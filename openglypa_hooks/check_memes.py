import re

func_reg = r"async def generate_meme(?:.|\n)*return byte_io\.read\(\)"
select_reg = r"select = random\.randint\((\d*?), (\d*?)\)"
ifs_reg = r"if select == (\d*?):"


def main() -> int:

    with open("utils/images.py", "rb") as f:
        content = str(f.read())
        function = re.search(func_reg, content).string
        select = re.search(select_reg, function)
        a = select.group(1)
        b = select.group(2)

        if a == b:
            print("В select = rendom.randint a равен b")
            return 1

        ifs = re.findall(ifs_reg, function)
        found = False
        for i in ifs:
            if int(i) not in range(int(a), int(b)+1):
                found = True
                print(f"Мем под select = {i} не входит в диапозон выбора")

        if found:
            return 1
        else:
            return 0


if __name__ == "__main__":
    raise SystemExit(main())