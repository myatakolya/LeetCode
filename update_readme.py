#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path
from typing import List, Dict, Optional

def parse_solution_file(file_path: Path) -> Optional[Dict[str, str]]:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        pattern = r'''
            Problem:\s*(.+?)\n
            Number:\s*(\d+)\s*\n
            Difficulty:\s*(Easy|Medium|Hard)\s*\n
            Time\s*Complexity:\s*(.+?)\n
            Space\s*Complexity:\s*(.+?)\n
            URL:\s*(https?://[^\s]+)(?:\n\s*Topics:\s*(.+?))?(?:\n|$)
        '''
        
        match = re.search(pattern, content, re.VERBOSE | re.IGNORECASE)
        if not match:
            print(f"⚠️  Пропускаем {file_path.name}: метаданные не найдены")
            return None
        
        return {
            'name': match.group(1).strip(),
            'number': match.group(2).strip(),
            'difficulty': match.group(3).strip().capitalize(),
            'time': match.group(4).strip(),
            'space': match.group(5).strip(),
            'url': match.group(6).strip(),
            'topics': match.group(7).strip() if match.group(7) else '',
            'file': file_path.name,
            'path': str(file_path)
        }
    except Exception as e:
        print(f"❌ Ошибка при чтении {file_path.name}: {e}")
        return None

def collect_solutions(base_dir: str = '.') -> List[Dict[str, str]]:
    """
    Собирает все решения из папок Easy, Medium, Hard.
    """
    solutions = []
    difficulties = ['Easy', 'Medium', 'Hard']
    
    for diff in difficulties:
        folder = Path(base_dir) / diff
        if not folder.exists():
            print(f"⚠️  Папка {folder} не найдена, пропускаем")
            continue
        
        # Ищем все Python файлы
        for file_path in folder.glob('*.py'):
            solution = parse_solution_file(file_path)
            if solution:
                # Проверяем, что сложность совпадает с папкой
                if solution['difficulty'] != diff:
                    print(f"⚠️  {file_path.name}: сложность в файле ({solution['difficulty']}) "
                          f"не совпадает с папкой ({diff})")
                solutions.append(solution)
    
    # Сортируем по номеру задачи
    return sorted(solutions, key=lambda x: int(x['number']))

def generate_table(solutions: List[Dict[str, str]]) -> str:
    if not solutions:
        return "Пока нет решений. 😅"
    
    difficulty_emojis = {'Easy': '🟢', 'Medium': '🟡', 'Hard': '🔴'}
    grouped = {'Easy': [], 'Medium': [], 'Hard': []}
    for sol in solutions:
        grouped[sol['difficulty']].append(sol)
    
    table_parts = []
    for difficulty in ['Easy', 'Medium', 'Hard']:
        if not grouped[difficulty]:
            continue
        emoji = difficulty_emojis.get(difficulty, '⚪')
        table_parts.append(f"\n### {emoji} {difficulty}\n")
        table_parts.append(
            "| # | Название | Время | Память | Темы | Решение |\n"
            "|---|----------|-------|--------|------|---------|"
        )
        for sol in grouped[difficulty]:
            file_link = f"./{sol['path']}"
            row = (
                f"| {sol['number']} "
                f"| [{sol['name']}]({sol['url']}) "
                f"| `{sol['time']}` "
                f"| `{sol['space']}` "
                f"| {sol['topics']} "
                f"| [📄]({file_link}) |"
            )
            table_parts.append(row)
    return "\n".join(table_parts)

def update_readme(readme_path: str = 'README.md', solutions: List[Dict[str, str]] = None):
    """
    Обновляет README.md, заменяя секцию с таблицей решений.
    """
    if solutions is None:
        solutions = collect_solutions()
    
    # Генерируем таблицу
    table = generate_table(solutions)
    
    # Читаем текущий README
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Файл {readme_path} не найден!")
        return
    
    # Маркеры для замены
    start_marker = "<!-- SOLUTIONS_TABLE_START -->"
    end_marker = "<!-- SOLUTIONS_TABLE_END -->"
    
    # Если маркеры есть - заменяем
    if start_marker in content and end_marker in content:
        pattern = f"{start_marker}.*?{end_marker}"
        replacement = f"{start_marker}\n\n{table}\n\n{end_marker}"
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    else:
        # Если маркеров нет - добавляем в конец
        print("⚠️  Маркеры не найдены, добавляем таблицу в конец файла")
        new_content = content + f"\n\n## 📊 Таблица решений\n\n{start_marker}\n\n{table}\n\n{end_marker}\n"
    
    # Сохраняем
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ README.md успешно обновлен! Найдено {len(solutions)} решений.")

def main():
    """
    Основная функция.
    """
    print("🚀 Генерация таблицы решений LeetCode...")
    
    # Собираем решения
    solutions = collect_solutions()
    
    if not solutions:
        print("❌ Решения не найдены. Убедитесь, что файлы содержат метаданные.")
        print("   Пример метаданных в начале файла:")
        print('   """')
        print('   Problem: Two Sum')
        print('   Number: 1')
        print('   Difficulty: Easy')
        print('   Time Complexity: O(n)')
        print('   Space Complexity: O(n)')
        print('   URL: https://leetcode.com/problems/two-sum/')
        print('   """')
        return
    
    print(f"📊 Найдено {len(solutions)} решений:")
    for sol in solutions:
        print(f"   - #{sol['number']}: {sol['name']} ({sol['difficulty']})")
    
    # Обновляем README
    update_readme(solutions=solutions)
    
    print("✅ Готово!")

if __name__ == "__main__":
    main()
