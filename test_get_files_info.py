from functions.get_files_info import get_files_info

def test_get_files_info():
    print("Result for current directory:")
    res = get_files_info("calculator", ".")
    print("\n".join("  " + line for line in res.splitlines()))
    print()

    print("Result for 'pkg' directory:")
    res = get_files_info("calculator", "pkg")
    print("\n".join("  " + line for line in res.splitlines()))
    print()

    print("Result for '/bin' directory:")
    res = get_files_info("calculator", "/bin")
    print("\n".join("  " + line for line in res.splitlines()))
    print()

    print("Result for '../' directory:")
    res = get_files_info("calculator", "../")
    print("\n".join("  " + line for line in res.splitlines()))
    print()
    
if __name__ == "__main__":
    test_get_files_info()