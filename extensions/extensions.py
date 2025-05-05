fname = input("File name: ").strip()
type = fname.rsplit(".", 1)  

if len(type) < 2:
    print("application/octet-stream")
else:
    extension = type[1].lower()
    match extension:
        case "gif" | "jpg" | "jpeg" | "png":
            if extension == "jpg":
                extension = "jpeg"
            print(f"image/{extension}")
        case "pdf" | "zip":
            print(f"application/{extension}")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")
