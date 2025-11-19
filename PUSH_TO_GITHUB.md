# 🚀 راهنمای Push به GitHub

## مرحله 1: ایجاد Repository در GitHub

1. به آدرس زیر بروید:
   **https://github.com/new**

2. اطلاعات زیر را وارد کنید:
   - **Repository name**: `WebSiteEhsanLak`
   - **Description**: "وب‌سایت شخصی احسان لک - پورتفولیو، بلاگ و دوره‌های آموزشی با Django"
   - **Visibility**: Public یا Private (انتخاب شما)
   - ⚠️ **مهم**: تیک "Initialize this repository with a README" را **نزنید**
   - ⚠️ **مهم**: تیک "Add .gitignore" را **نزنید**
   - ⚠️ **مهم**: تیک "Choose a license" را **نزنید**

3. روی دکمه **"Create repository"** کلیک کنید

---

## مرحله 2: Push کردن کد

بعد از ایجاد repository، دستور زیر را اجرا کنید:

```bash
git push -u origin main
```

یا اگر از SSH استفاده می‌کنید و authentication تنظیم شده:

```bash
git push -u origin main
```

---

## ✅ بعد از Push

پروژه شما در آدرس زیر در دسترس خواهد بود:
**https://github.com/Ehsunpy/WebSiteEhsanLak**

---

## 🔐 اگر Authentication نیاز دارید:

اگر push با خطا مواجه شد، باید authentication را تنظیم کنید:

### روش 1: Personal Access Token
1. به Settings > Developer settings > Personal access tokens > Tokens (classic) بروید
2. یک token جدید ایجاد کنید
3. هنگام push، از token به جای password استفاده کنید

### روش 2: SSH Key
1. SSH key را به GitHub اضافه کنید
2. Remote را به SSH تغییر دهید:
   ```bash
   git remote set-url origin git@github.com:Ehsunpy/WebSiteEhsanLak.git
   ```

---

**بعد از ایجاد repository، به من بگویید تا push کنم!** 🎉

