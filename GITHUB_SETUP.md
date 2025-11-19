# راهنمای اضافه کردن پروژه به GitHub

## مراحل:

### 1️⃣ ایجاد Repository در GitHub

1. به آدرس زیر بروید:
   https://github.com/new

2. اطلاعات زیر را وارد کنید:
   - **Repository name**: `EHSAN-WEB` یا `ehsan-portfolio` (یا هر نامی که می‌خواهید)
   - **Description**: "وب‌سایت شخصی احسان لک - پورتفولیو، بلاگ و دوره‌های آموزشی"
   - **Visibility**: Public یا Private (انتخاب شما)
   - **⚠️ مهم**: تیک "Initialize this repository with a README" را **نزنید** (چون ما قبلاً README داریم)

3. روی دکمه **"Create repository"** کلیک کنید

### 2️⃣ اضافه کردن Remote و Push

بعد از ایجاد repository، دستورات زیر را اجرا کنید:

```bash
# اضافه کردن remote (نام repository را جایگزین کنید)
git remote add origin https://github.com/Ehsunpy/REPOSITORY_NAME.git

# تغییر نام branch به main
git branch -M main

# Push به GitHub
git push -u origin main
```

یا اگر از SSH استفاده می‌کنید:
```bash
git remote add origin git@github.com:Ehsunpy/REPOSITORY_NAME.git
git branch -M main
git push -u origin main
```

---

## یا اگر می‌خواهید من این کار را انجام دهم:

فقط نام repository را که در GitHub ایجاد کردید به من بگویید تا remote را اضافه کنم و push کنم.

