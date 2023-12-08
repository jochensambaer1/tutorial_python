class StudentDeveloperPack:
    def __init__(self, name, university):
        self.name = name
        self.university = university
        self.tools = []

    def add_tool(self, tool):
        self.tools.append(tool)

    def get_tools(self):
        return self.tools

# Example usage:
pack = StudentDeveloperPack("John Doe", "University of Example")
pack.add_tool("GitHub")
pack.add_tool("Visual Studio Code")
pack.add_tool("Python")
print(pack.get_tools())
