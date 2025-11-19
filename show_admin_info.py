#!/usr/bin/env python
"""
اسکریپت نمایش اطلاعات اکانت ادمین
"""
import os
import sys
import django

# تنظیم Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ehsan_site.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

print("\n" + "="*60)
print("🔐 اطلاعات اکانت‌های ادمین:")
print("="*60 + "\n")

superusers = User.objects.filter(is_superuser=True)

if superusers.exists():
    for user in superusers:
        print(f"👤 Username: {user.username}")
        print(f"📧 Email: {user.email}")
        print(f"✅ Superuser: {'بله' if user.is_superuser else 'خیر'}")
        print(f"🔑 Staff: {'بله' if user.is_staff else 'خیر'}")
        print("-" * 60)
else:
    print("⚠️  هیچ اکانت ادمینی یافت نشد!")
    print("\nبرای ایجاد اکانت ادمین، دستور زیر را اجرا کنید:")
    print("python manage.py createsuperuser\n")

print("\n🌐 برای ورود به پنل مدیریت:")
print("   1. سرور را اجرا کنید: python manage.py runserver")
print("   2. به آدرس زیر بروید: http://127.0.0.1:8000/admin/")
print("   3. با Username و Password بالا وارد شوید\n")

