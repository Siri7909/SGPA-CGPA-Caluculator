#!/usr/bin/env python3
"""
Simple SGPA & CGPA CLI calculator.
Usage:
 - Run the script and follow prompts.
 - Default grade mapping is 10-point: A+ 10, A 9, B+ 8, B 7, C 6, D 5, F 0
"""
import sys

GRADE_MAP = {
    'A+': 10.0, 'A': 9.0, 'B+': 8.0, 'B': 7.0, 'C': 6.0, 'D': 5.0, 'F': 0.0
}

def input_float(prompt, default=None):
    while True:
        s = input(prompt).strip()
        if s == '' and default is not None:
            return default
        try:
            return float(s)
        except ValueError:
            print("Enter a number.")

def calc_sgpa():
    print("\nEnter courses for semester. Leave course name empty to finish.")
    total_credits = 0.0
    weighted = 0.0
    while True:
        name = input("Course name (blank to finish): ").strip()
        if not name:
            break
        credits = input_float("  Credits: ")
        grade = input("  Grade (A+, A, B+, B, C, D, F): ").strip().upper()
        if grade not in GRADE_MAP:
            print("  Unknown grade, please use one of:", ', '.join(GRADE_MAP.keys()))
            continue
        gp = GRADE_MAP[grade]
        total_credits += credits
        weighted += credits * gp
    if total_credits == 0:
        print("No credits entered.")
        return None, None
    sgpa = weighted / total_credits
    print(f"SGPA = {sgpa:.3f}  (Total credits: {total_credits})")
    return sgpa, total_credits

def main():
    print("SGPA & CGPA CLI Calculator")
    semesters = []
    while True:
        print("\nOptions:\n1) Calculate SGPA for a semester\n2) Add existing semester SGPA (quick)\n3) Compute CGPA\n4) Show saved semesters\n5) Exit")
        choice = input("Choose [1-5]: ").strip()
        if choice == '1':
            sgpa, credits = calc_sgpa()
            if sgpa is not None:
                name = input("Semester name (optional): ").strip() or f"Sem {len(semesters)+1}"
                semesters.append((name, sgpa, credits))
        elif choice == '2':
            name = input("Semester name: ").strip() or f"Sem {len(semesters)+1}"
            sgpa = input_float("SGPA: ")
            credits = input_float("Total credits for semester: ")
            semesters.append((name, sgpa, credits))
        elif choice == '3':
            if not semesters:
                print("No semesters added.")
                continue
            total_credits = sum(c for _, _, c in semesters)
            if total_credits == 0:
                print("Total credits are zero.")
                continue
            weighted = sum(sgpa * c for _, sgpa, c in semesters)
            cgpa = weighted / total_credits
            print("\nSaved semesters:")
            for n, s, c in semesters:
                print(f"  {n}: SGPA={s:.3f}, credits={c}")
            print(f"\nCGPA = {cgpa:.3f}  (Total credits: {total_credits})")
        elif choice == '4':
            if not semesters:
                print("No saved semesters.")
            else:
                for n, s, c in semesters:
                    print(f"  {n}: SGPA={s:.3f}, credits={c}")
        elif choice == '5':
            print("Bye.")
            sys.exit(0)
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
