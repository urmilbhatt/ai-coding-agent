from functions.get_files_info import get_files_info

def run_tests():
    print('get_files_info("calculator", "."):')
    print('Result for current directory:')
    print(get_files_info("calculator", "."))
    print()

    print('get_files_info("calculator", "pkg"):')
    print("Result for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))
    print()

    print('get_files_info("calculator", "/bin"):')
    print('Result for \'/bin\' directory:')
    print("   " + get_files_info("calculator", "/bin"))
    print()

    print('get_files_info("calculator", "../"):')
    print('Result for \'../\' directory:')
    print("   " + get_files_info("calculator", "../"))
    print()

if __name__ == "__main__":
    run_tests()
