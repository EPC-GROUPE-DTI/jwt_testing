import sys
import json
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QTextEdit, QLabel, QFileDialog, QMessageBox
)
from PyQt6.QtCore import Qt
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import jwt


class JWTApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.private_key = None
        self.public_key = None
        self.private_key_pem = None
        self.public_key_pem = None

    def init_ui(self):
        self.setWindowTitle("JWT Generator/Decoder")
        self.resize(800, 600)

        layout = QVBoxLayout()

        # Key generation buttons and text edits
        key_layout = QHBoxLayout()
        self.btn_generate_keys = QPushButton("Generate Random RSA Keys")
        self.btn_import_keys = QPushButton("Import Keys")
        self.btn_export_keys = QPushButton("Export Keys")
        self.btn_export_keys.setEnabled(False)
        self.btn_generate_keys.clicked.connect(self.generate_keys)
        self.btn_import_keys.clicked.connect(self.import_keys)
        self.btn_export_keys.clicked.connect(self.export_keys)

        key_layout.addWidget(self.btn_generate_keys)
        key_layout.addWidget(self.btn_import_keys)
        key_layout.addWidget(self.btn_export_keys)

        self.txt_public_key = QTextEdit()
        self.txt_public_key.setReadOnly(True)
        self.txt_public_key.setPlaceholderText("Public Generated RSA Key")

        self.txt_private_key = QTextEdit()
        self.txt_private_key.setReadOnly(True)
        self.txt_private_key.setPlaceholderText("Private Generated RSA Key")

        layout.addLayout(key_layout)
        layout.addWidget(QLabel("Public Key:"))
        layout.addWidget(self.txt_public_key)
        layout.addWidget(QLabel("Private Key:"))
        layout.addWidget(self.txt_private_key)

        # JWT encoding/decoding buttons and text edits
        jwt_layout = QHBoxLayout()
        self.btn_encode_jwt = QPushButton("Encode JWT")
        self.btn_decode_jwt = QPushButton("Decode JWT")
        self.btn_encode_jwt.clicked.connect(self.encode_jwt)
        self.btn_decode_jwt.clicked.connect(self.decode_jwt)

        jwt_layout.addWidget(self.btn_encode_jwt)
        jwt_layout.addWidget(self.btn_decode_jwt)

        self.txt_json_payload = QTextEdit()
        self.txt_json_payload.setPlaceholderText("JSON of JWT")

        self.txt_encoded_jwt = QTextEdit()
        self.txt_encoded_jwt.setPlaceholderText("Encoded JWT")

        layout.addLayout(jwt_layout)
        layout.addWidget(QLabel("JSON Payload:"))
        layout.addWidget(self.txt_json_payload)
        layout.addWidget(QLabel("Encoded JWT:"))
        layout.addWidget(self.txt_encoded_jwt)

        self.setLayout(layout)

    def generate_keys(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()

        private_key_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_key_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        self.private_key_pem = private_key_pem.decode("utf-8")
        self.public_key_pem = public_key_pem.decode("utf-8")

        self.txt_private_key.setText(self.private_key_pem)
        self.txt_public_key.setText(self.public_key_pem)
        self.btn_export_keys.setEnabled(True)

    def import_keys(self):
        private_file, _ = QFileDialog.getOpenFileName(self, "Open Private Key", "", "PEM Files (*.pem)")
        public_file, _ = QFileDialog.getOpenFileName(self, "Open Public Key", "", "PEM Files (*.pem)")

        if private_file and public_file:
            try:
                with open(private_file, "rb") as f:
                    private_key_pem = f.read()
                with open(public_file, "rb") as f:
                    public_key_pem = f.read()

                # Load the private and public keys from the PEM files
                self.private_key = serialization.load_pem_private_key(private_key_pem, password=None)
                self.public_key = serialization.load_pem_public_key(public_key_pem)

                self.private_key_pem = private_key_pem.decode("utf-8")
                self.public_key_pem = public_key_pem.decode("utf-8")

                self.txt_private_key.setText(self.private_key_pem)
                self.txt_public_key.setText(self.public_key_pem)
                self.btn_export_keys.setEnabled(True)

                QMessageBox.information(self, "Keys Imported", "Private and public keys were successfully imported.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to import keys: {e}")

    def export_keys(self):
        if not self.private_key or not self.public_key:
            QMessageBox.warning(self, "Warning", "No keys to export. Generate keys first.")
            return

        options = QFileDialog.Options()
        private_file, _ = QFileDialog.getSaveFileName(self, "Save Private Key", "", "PEM Files (*.pem)", options=options)
        public_file, _ = QFileDialog.getSaveFileName(self, "Save Public Key", "", "PEM Files (*.pem)", options=options)

        if private_file and public_file:
            with open(private_file, "wb") as f:
                f.write(self.txt_private_key.toPlainText().encode("utf-8"))
            with open(public_file, "wb") as f:
                f.write(self.txt_public_key.toPlainText().encode("utf-8"))
            QMessageBox.information(self, "Export Success", "Keys exported successfully.")

    def encode_jwt(self):
        if not self.private_key:
            QMessageBox.warning(self, "Warning", "No private key found. Generate or import keys first.")
            return

        try:
            json_payload = json.loads(self.txt_json_payload.toPlainText())
            # Use the private key PEM string for encoding
            token = jwt.encode(json_payload, self.private_key_pem, algorithm="RS256")
            self.txt_encoded_jwt.setText(token)
        except json.JSONDecodeError:
            QMessageBox.critical(self, "Error", "Invalid JSON payload.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to encode JWT: {e}")

    def decode_jwt(self):
        if not self.public_key:
            QMessageBox.warning(self, "Warning", "No public key found. Generate or import keys first.")
            return

        try:
            token = self.txt_encoded_jwt.toPlainText()
            # Use the public key PEM string for decoding
            decoded_payload = jwt.decode(token, self.public_key_pem, algorithms=["RS256"], options={"verify_aud": False, "verify_signature": True})
            self.txt_json_payload.setText(json.dumps(decoded_payload, indent=4))
        except jwt.exceptions.DecodeError:
            QMessageBox.critical(self, "Error", "Invalid JWT token.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to decode JWT: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JWTApp()
    window.show()
    sys.exit(app.exec())
