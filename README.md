# E-Card-Generator

A Flask-based web application for generating and managing digital versions of key Indian identity cards: Aadhar, PAN, Driving License, and Voter ID.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)

## Overview

E-Card-Generator streamlines the process of requesting and managing digital versions of essential Indian identity documents. The application provides a complete workflow from user registration to card generation, with an admin interface for verification and approval.

## Features

- **User Authentication**: Secure registration and login system
- **Multiple Card Types**: Support for Aadhar, PAN, Driving License, and Voter ID cards
- **Request Management**: Complete lifecycle tracking from request to generation
- **Admin Dashboard**: Tools for managing users and card requests
- **Automated Key Generation**: Unique algorithms for each card type
- **Status Tracking**: Monitor progress (requested, under verification, verified, generated)
- **File Upload**: Support for user images and documents
- **Search Functionality**: Find users and filter by card status

## Card Key Generation

Each identity card uses a unique algorithm for generating its identifier:

| Card Type | Format | Example | Generation Logic |
|-----------|--------|---------|-----------------|
| Aadhar | 12-digit number | 123456789012 | Random 12-digit integer |
| PAN | XJHQR3842P | XJHQR3842P | 5 uppercase letters, 4 digits, 1 uppercase letter |
| Voter ID | ABC1234567 | ABC1234567 | 3 uppercase letters + 7 digits |
| Driving License | DL-01-2025-1234567 | DL-01-2025-1234567 | 2 letters (state) + 2 digits (RTO) + year + 7 digits |

## Directory Structure

```
E-Card-Generator/
├── README.md
├── app.py                 # Main application entry point
├── key_generator.py       # Card number generation algorithms
├── test.txt
├── Application/           # Core application modules
│   ├── controllers.py     # Route handlers and business logic
│   ├── database.py        # Database connection and utilities
│   ├── models.py          # Data models
│   └── __pycache__/
├── instance/
│   └── ecard.sqlite       # SQLite database
├── static/                # Static assets
│   ├── pan.webp
│   └── style.css
└── templates/             # HTML templates
    ├── Aadhar.html
    ├── admin_dashboard.html
    ├── card_requirements.txt
    ├── driving-license.html
    ├── login.html
    ├── pan-card.html
    ├── Register.html
    ├── results.html
    ├── select.html
    ├── summary.html
    ├── update_status.html
    ├── user_dashboard.html
    ├── view_aadhar.html
    ├── view_driving.html
    ├── view_pan.html
    ├── view_voterid.html
    └── voter-id.html
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/E-Card-Generator.git
   cd E-Card-Generator
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables (if needed):
   ```bash
   # Example for development
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```

## Running the Application

Start the application with:

```bash
python app.py
```

The application will be available at http://127.0.0.1:5000/

## Usage Guide

### For Users

1. **Registration and Login**:
   - Register with a valid email and password
   - Log in using your credentials

2. **Requesting Cards**:
   - Select the card type you need (Aadhar, PAN, Driving License, or Voter ID)
   - Fill in the required personal information
   - Upload necessary documents and photos
   - Submit your request

3. **Tracking Status**:
   - View all your card requests on your dashboard
   - Check the status of each request (requested, under verification, verified, generated)
   - Download generated cards once approved

### For Administrators

1. **Admin Dashboard**:
   - Access the admin interface via `/admin` (login with admin credentials)
   - View all user requests across the system

2. **Request Management**:
   - Review pending requests
   - Verify user information and uploaded documents
   - Update request status (under verification, verified, rejected)
   - Generate card numbers for approved requests

3. **User Management**:
   - View and search for users
   - Manage user accounts and permissions

## API Reference

The application does not currently expose a public API, but internal endpoints are available for the web interface.

## Development

### Prerequisites

- Python 3.6+
- Flask and its dependencies
- SQLite

### Setting Up a Development Environment

Follow the installation instructions above, then:

1. Enable debug mode:
   ```bash
   export FLASK_DEBUG=1
   ```

2. Make code changes as needed

3. Run tests:
   ```bash
   # Test command (if tests are implemented)
   ```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask documentation and community
- SQLite for database support
- All contributors and users of the application

## Contact

For questions or support, please contact [work.aayushkotwani@gmail.com](mailto:work.aayushkotwani@gmail.com)
