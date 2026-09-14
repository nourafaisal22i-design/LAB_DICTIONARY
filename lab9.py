phone = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}

num = input("Enter phone number: ")

if len(num) != 10 or not num.isdigit():
    print("This is invalid number")
elif num in phone:
    print(phone[num])
else:
    print("Sorry, the number is not found")
