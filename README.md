# BinCat | Under development (no estable version)

BinCat is a library for secure token management, designed to integrate easily into Python applications. It provides tools to generate, validate, and revoke tokens using an SQLite database and Fernet encryption.

## Installation

Install BinCat directly from PyPI (coming soon) or clone the repository and install it locally:

```bash
pip install bincat
```

## Features

- **Secure token generation:** Uses Fernet encryption to ensure security.
- **Validation and revocation:** Ensures that only authorized tokens can operate.
- **SQLite database:** Lightweight and efficient storage for token management.

## Usage

### Initialize the token manager

```python
from bincat.token_manager import TokenManager

# Initialize the manager with a database
manager = TokenManager('database.db')
```

### Generate a token

```python
token = manager.generate_token('user123')
print(f'Token generated: {token}')
```

### Validate a token

```python
is_valid = manager.validate_token(token)
print(f'Is the token valid? {is_valid}')
```

### Revoke a token

```python
manager.revoke_token(token)
print('Token successfully revoked.')
```

## Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a branch for your feature: `git checkout -b new-feature`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Submit a pull request.

## License

BinCat is available under the MIT license. See the `LICENSE` file for more details.

## Contact

If you have any questions or suggestions, feel free to open an issue on the [GitHub repository](https://github.com/eduolihez/BinCat).
