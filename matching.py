# NAME:         Nicholas Ngobi

# ASSIGNMENT:  stacks and Queues

from Stack import Stack

# Returns True if the braces match,
# & False otherwise
def matcher(str):
    s = Stack([])
    opening=["(", "[" ,"{"]
    closing=[")","]", "}"]
    for char in str:
        if char in opening:
            s.push(char)
        elif char in closing:
            if s.is_empty():
                return False
            top= s.pop()
        if (char==")" and top!="(" )or (char=="]" and top!="[") or (char=="}" and top!="{"):
            return False
    
    return s.is_empty()
    

def main():
    print("matcher: ", matcher("[()]"))

# Don't run main on import
if __name__ == "__main__":
    main()

