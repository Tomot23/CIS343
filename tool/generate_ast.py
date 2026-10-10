import sys

class GenerateAst():

    def main():
        if len(sys.argv) != 2:
            print("Usage: python generate_ast <output directory>")
            sys.exit(64)
        output_dir = sys.argv[1]

        GenerateAst.define_ast(output_dir, "Expr", [
            "Binary     = left: Expr, operator: Token, right: Expr",
            "Grouping   = expression: Expr",
            "Literal    = value: object",
            "Unary      = operator: Token, right: Expr"
        ])
        
    def define_ast(output_dir: str, base_name:str, types: list[str]):
        path = output_dir + base_name + ".py"
        with open(path, "w") as f:
            f.write("from scyode_token import Token\n")
            f.write("from abc import ABC, abstractmethod\n\n\n")

            f.write("class " + base_name + ":\n")

            GenerateAst.define_visitor(f, base_name, types)

            f.write("\n\t@abstractmethod\n")
            f.write("\tdef accept(vistor: Visitor): pass\n\n")

            for type in types:
                class_name = type.split('=')[0].strip()
                fields = type.split('=')[1].strip()
                GenerateAst.define_type(f, base_name, class_name, fields)
                f.write("\n")

    def define_type(writer, base_name: str, class_name:str, field_list:str):
        writer.write("\tclass " + class_name + ":\n")

        writer.write("\t\tdef __init__(self, " + field_list + "):\n")

        fields = field_list.split(", ")
        for field in fields:
            name = field.split(": ")[0]
            writer.write("\t\t\tself." + name + " = " + name + "\n")

        writer.write("\n\t\tdef accept(self, visitor: " + base_name + ".Visitor):\n")
        writer.write("\t\t\treturn visitor.visit_" + class_name.lower()
                      + "_" + base_name.lower() + "(self)\n")

    def define_visitor(writer, base_name:str, types:list[str]):
        writer.write("\tclass Visitor(ABC):\n")

        for type in types:
            type_name = type.split("=")[0].strip()
            writer.write("\t\t@abstractmethod\n")
            writer.write("\t\tdef visit_" + type_name.lower() + "_" + 
                         base_name.lower() + "(" + base_name.lower() + 
                         ": " + base_name + "." + type_name + "): pass\n")

if __name__ == "__main__":
    GenerateAst.main()