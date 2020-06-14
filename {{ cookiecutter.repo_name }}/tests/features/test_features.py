from {{ cookiecutter.package_name }}.features import placeholder


def test_placeholder():
    """Ensure placeholder function runs without failure"""
    placeholder()
