a = "hello"
b = 'world'
c = '''a multiple
line string'''
d = """More
multiple"""
e = ("Three " "Strings " "Together")    #Automatic concatenation when there are no commas
f = ("Three ", "Strings ", "Separate")

s = "hello world, how are you"
s2 = s.split(" ")
s2
"#".join(s2)
s.replace(' ', '#')
s.partition(' ')

classname = "MyClass"
python_code = "print('hello world')"
template = f"""
public class {classname} {{
    public static void main(String[] args) {{
        System.out.println("{python_code}");
    }}
}}"""   #Use single braces {} to have python replace the contents with the respective parameter; use double braces {{}} to have python return single braces without replacing the contents
print(template)

emails = ("a@example.com", "b@example.com")
message = {
    "subject": "You Have Mail?",
    "message": "Here's some mail for you!",
}

formatted = f"""
From: <{emails[0]}>
To: <{emails[1]}>
Subject: {message['subject']}
{message['message']}"""
print(formatted)

emails = ("c@example.com", "d@example.com")
message = {
    "subject": "More Mail?",
    "message": "Why is there so much mail?",
}
print(formatted)    #Does not automatically update; uses the parameters from when the format code was originally run

class Email:
    def __init__(self, from_addr, to_addr, subject, message):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self.message = message

    def message(self):
        return self._message

    def formatted(self):
        fmt = f"""From: <{email.from_addr}>
To: <{email.to_addr}>
Subject: {email.subject}
{email.message}"""
        print(fmt)

email = Email(
    "a@example.com",
    "b@example.com",
    "You Have Mail!",
    "Here's some mail for you!",
)

email.formatted()

f"['a' for a in range(5)]"
f"{'yes' if True else 'no'}"

subtotal = 12.32
tax = subtotal * 0.07
total = subtotal + tax
print("Sub: ${0} Tax: ${1} Total: ${total}".format(subtotal, tax, total=total))
print("Sub: ${0:0.2f} Tax: ${1:0.2f} Total: ${total:0.2f}".format(subtotal, tax, total=total))

orders = [("burger", 2, 5), ("fries", 3.5, 1), ("cola", 1.75, 3)]
print("PRODUCT  QUANTITY    PRICE   SUBTOTAL")
for product, price, quantity in orders:
    subtotal = price * quantity
    print(
        f"{product:10s}{quantity: ^9d}"
        f"${price: <8.2f}${subtotal: >7.2f}"
    )

characters = b'\x63\x6c\x69\x63\x68\xe9'
print(characters)
print(characters.decode("latin-1"))
characters = characters.decode("latin-1")
print(characters.encode("UTF-8"))
print(characters.encode("latin-1"))
print(characters.encode("CP437"))
print(characters.encode("ascii"))
