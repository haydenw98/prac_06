from Programming_language import ProgrammingLanguages

ruby = ProgrammingLanguages("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguages("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguages("Visual Basic", "Static", False, 1991)
java = ProgrammingLanguages("Java", "Static", True, 1995)

def main():
    languages = [ruby, python, visual_basic, java]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.check_dynamic():
            print(language.name)
    for language in languages:
        print(language)

main()