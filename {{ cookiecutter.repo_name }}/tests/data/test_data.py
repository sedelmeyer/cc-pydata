from {{ cookiecutter.package_name }}.data import placeholder


def test_placeholder():
    """Ensure placeholder function runs without failure"""
    placeholder()
