import black
import subprocess

def format_python(code: str) -> str:
    try:
        formatted_code = black.format_str(code, mode=black.Mode())
        return formatted_code
    except Exception as e:
        raise Exception(f"Python formatting failed: {str(e)}")
    

def format_c(code: str) -> str:
    try:
        # Write code to a temporary file for clang-format to read
        with open("temp.c", "w") as temp_file:
            temp_file.write(code)

        # Run clang-format
        subprocess.run(["clang-format", "-i", "temp.c"], check=True)

        # Read the formatted code back from the file
        with open("temp.c", "r") as temp_file:
            formatted_code = temp_file.read()

        return formatted_code
    except Exception as e:
        raise Exception(f"C formatting failed: {str(e)}")
    

GOOGLE_JAVA_FORMAT_JAR = "google-java-format-1.15.0-all-deps.jar"
    
def format_java(code: str) -> str:
    try:
        # Write code to a temporary file for Google Java Format to read
        with open("temp.java", "w") as temp_file:
            temp_file.write(code)

        # Run Google Java Format
        subprocess.run(
            ["java", "-jar", GOOGLE_JAVA_FORMAT_JAR, "--replace", "temp.java"],
            check=True
        )

        # Read the formatted code back from the file
        with open("temp.java", "r") as temp_file:
            formatted_code = temp_file.read()

        return formatted_code
    except Exception as e:
        raise Exception(f"Java formatting failed: {str(e)}")