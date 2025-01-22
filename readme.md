# JWT Generator/Decoder Application

This is a Python-based graphical application used for testing JWT (JSON Web Tokens) encoding and decoding with RSA encryption. The application allows you to:

- Generate and display RSA private and public keys.
- Import existing RSA keys from PEM files.
- Export RSA keys to PEM files.
- Encode JWTs using an RSA private key.
- Decode JWTs using an RSA public key.

## Features

- **Generate RSA Keys**: Generate RSA public and private keys dynamically for testing.
- **Import and Export Keys**: Import and export RSA keys in PEM format.
- **Encode JWT**: Encode a JSON payload to a JWT using the RSA private key.
- **Decode JWT**: Decode a JWT using the RSA public key.

## Requirements

This application uses the following Python packages:

- `PyQt6`: For creating the GUI.
- `cryptography`: For RSA key generation and key management.
- `pyjwt`: For encoding and decoding JWTs.

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```
## How to Generate `requirements.txt`

To generate the `requirements.txt` file for your project:

1. Ensure that you have activated your virtual environment (if using one).
2. Run the following command to generate `requirements.txt`:

```
pip freeze > requirements.txt
```

## Installation and Usage

### Install Dependencies

Before running the application, make sure to install the required libraries:

```
pip install -r requirements.txt
```
    
# JWT Generator/Decoder Application

## Run the Application

To start the application, run the following command:

```
python main.py
```

# JWT Generator/Decoder Application

## GUI Overview

- **RSA Key Generation**: You can generate RSA keys (public and private) and view them in the text areas.
- **Key Import/Export**: You can import or export keys in PEM format using the provided buttons.
- **JWT Encoding/Decoding**: Input a JSON payload, encode it into a JWT, or decode an existing JWT.

## How It Works

### Key Generation

You can generate a pair of RSA keys (private and public). The keys will be displayed in the text boxes, and you can copy or export them as PEM files.

### JWT Encoding

After generating or importing keys, you can encode a JSON payload into a JWT. You need to input a valid JSON object into the "JSON Payload" text box. The encoded JWT will be displayed in the "Encoded JWT" text box.

### JWT Decoding

You can paste an encoded JWT into the "Encoded JWT" text box. After clicking the "Decode JWT" button, the payload will be decoded and displayed in the "JSON Payload" text box.

### Key Import/Export

You can import existing RSA keys from PEM files using the "Import Keys" button, or you can export the currently displayed keys to PEM files using the "Export Keys" button.

## Example

### JSON Payload:

```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}
```
## Generated JWT:

```text
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mzc1NTUzODIsImlhdCI6MTczNzQ2ODk4MiwianRpIjoiNTY4ODBjMDMtYzAwYi00NjY0LTlkZmYtNWE0OGYwZTBkZDRmIiwiaXNzIjoiaHR0cHM6Ly9leHBsb3JlLXN0YWdpbmcuZXBjLWdyb3VwZS5jb20vcmVhbG1zL3ZlcnRleCIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiJmZjQyOWFjNS1mN2Y4LTRlZjMtODFiMi1jZWEzYjRmNTBjZDQiLCJ0eXAiOiJCZWFyZXIiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cHM6Ly9leHBsb3JlLXN0YWdpbmcuZXBjLWdyb3VwZS5jb20iXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtdmVydGV4Iiwib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7IkVYUExPUkVfRlJPTlQiOnsicm9sZXMiOlsiZXhwbG9yZV9hcHBfdXNlciJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJlbWFpbCBwcm9maWxlIiwic2lkIjoiZWZmODQ2MWYtZWRmMC00NjgxLTkwNmEtNDhhN2Q3M2I5MmM2IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5hbWUiOiJBYmRlbG1vdW5lbSBBWkFJRVoiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJhYmRlbG1vdW5lbS5hemFpZXpAZXBjLWdyb3VwZS5jb20iLCJnaXZlbl9uYW1lIjoiQWJkZWxtb3VuZW0iLCJmYW1pbHlfbmFtZSI6IkFaQUlFWiIsImVtYWlsIjoiYWJkZWxtb3VuZW0uYXphaWV6QGVwYy1ncm91cGUuY29tIn0.t1cN37CvjuxBvpOjB4chtjveYUTu-FI9OuM7qkBSH6kz1ZFN3Xr1GaUJ3AomQpXstsPe7nDSgk29ggod9k4B7oz_JkDKCxoDU3bo_SQMKUr7oS9j5vupw4XBlkzT7JEUp6hApDT3lYTanWsW9um5-F-Wbkh174dtT4igoNeWk5XtR_hGqKe_18uEWxnKSNxgrbbAmUrfxTde0ePoENP-BH5tZdJTkC50yqAFPxThGjv8AsIzgB8qivDmMx3hhtv95HD4y2k9op_qtoSUNEKBZKxGI3nGQxsPo2RHu1y1u9bg4zJGvdIPlFNyDL9cTvXTi4XQXDwLFpntQN5dLo-kpg


