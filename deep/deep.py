x = input("what is the Answer to the Great Question of life, the uniberse, and Everything?").strip().lower()


match x :
    case "42" | "forty-two"|"forty two":
        print("yes")
    case _ :
        print("No")

