#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# Apply Python 3.14+ compatibility patch for Django admin
import sys
if sys.version_info >= (3, 14):
    try:
        print("🐍 Applying Python 3.14+ compatibility patch for Django admin...")
        from django.template import context
        
        # Store the original __copy__ method
        original_copy = context.BaseContext.__copy__
        
        # Create patched version that safely copies the context
        def patched_copy(self):
            duplicate = original_copy(self)
            # Handle different context implementations
            if hasattr(self, 'dicts'):
                duplicate.dicts = self.dicts[:]
            elif hasattr(self, '_dicts'):
                duplicate._dicts = self._dicts[:]
            return duplicate
        
        # Apply the patch
        context.BaseContext.__copy__ = patched_copy
        print("✅ Django admin patch applied successfully!")
    except Exception as e:
        print(f"⚠️ Warning: Could not apply patch: {e}")
        print("The admin panel might not work correctly.")

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ipswich_retail.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()