# **🌟 WA-VerifyAPI - Your Smart Solution for WhatsApp Group Link Validation!**  

🔗 **Welcome to WA-VerifyAPI!** A modern Flask-based API designed to effortlessly validate WhatsApp group links. With this cutting-edge technology, you can quickly extract group information and verify activity status. 🚀

✨ **Why choose WA-VerifyAPI?** Because we provide an efficient and reliable solution for your communication needs. Whether you're a developer looking to enhance your application or simply want to ensure the links you share are valid, we’ve got you covered! Join us and elevate your WhatsApp experience today! 🌈

## **✨ Features**  
✅ **Group Info Extraction** – Retrieve group name & profile picture (if available)  
✅ **Error Handling** – Detect expired, invalid, or fake links  
✅ **Fast & Scalable** – Built with **Flask** & **aiohttp** for async HTTP requests  
✅ **Link Validation** – Check if a WhatsApp group link is valid and active  
✅ **Modern API Standards** – Clean JSON responses with proper HTTP status codes 

## **🚀 Quick Start**
### **Prerequisites**
- Python 3.10+
- `pip` (Python package manager)

### **Installation**
1. Clone the repo:  
   ```sh
   git clone https://github.com/RozhakXD/WA-VerifyAPI.git
   cd WA-VerifyAPI
   ```

2. Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ```  

3. Run the API:  
   ```sh
   python run.py
   ```  

   The API will start at `http://localhost:5000`.

## **🌐 API Endpoints**
### **🔍 Validate a WhatsApp Group Link**
**`POST /api/validate`**
Check if a WhatsApp group link is valid and fetch group details.

#### **Request**
```json
{
    "link": "https://chat.whatsapp.com/EXAMPLE123"
}
```  

#### **Successful Response**
```json
{
    "status": "success",
    "data": {
        "link": "https://chat.whatsapp.com/EXAMPLE123",
        "groups_info": {
            "profile_picture": "https://pps.whatsapp.net/v/EXAMPLE_IMG",
            "group_name": "Awesome Tech Group"
        }
    }
}
```  

#### **Error Responses**
| Status | Description | Example Response |
|--------|-------------|------------------|
| `400` | Invalid URL format | `{"status": "error", "message": "Invalid WhatsApp group link"}` |
| `404` | Group not found/inactive | `{"status": "error", "message": "WhatsApp group is not active"}` |

## **🧪 Running Tests**
```sh
pytest tests/
```

## ☕ Support
If you love this project and want to support its development, you can make a donation on the following platforms:

[Trakteer](https://trakteer.id/rozhak_official/tip) | [PayPal](https://paypal.me/rozhak9) | [Saweria](https://saweria.co/rozhak9)

## **📜 License**
This project is licensed under **MIT License**.
