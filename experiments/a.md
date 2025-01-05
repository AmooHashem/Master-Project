
1. Scaling Application Servers and System Performance Tuning

```markdown
# آزمایش مدیریت منابع و مقیاس‌سازی سرورها

## اهداف
- آشنایی با بهینه‌سازی تنظیمات سیستم عامل برای افزایش کارایی سرورها
- درک محدودیت‌های پیش‌فرض سیستم و چگونگی رفع آنها

## نیازمندی‌ها
- سیستم لینوکس (ترجیحاً Ubuntu یا CentOS)
- دسترسی ادمین (root)
- آشنایی اولیه با خط فرمان لینوکس

## آزمایش عملی: بهینه‌سازی محدودیت فایل‌های باز

### مراحل
1. بررسی محدودیت فعلی فایل‌های باز
```bash
ulimit -n
```

2. تغییر محدودیت فایل‌های باز در فایل تنظیمات سیستم
```bash
sudo nano /etc/security/limits.conf
```
اضافه کنید:
```
* soft nofile 65535
* hard nofile 65535
```

3. اجرای تست با ابزارهایی مانند Apache Benchmark برای مقایسه عملکرد
4. مقایسه و تحلیل نتایج

## پرسش‌ها
- چه تأثیری در عملکرد سرور مشاهده کردید؟
- محدودیت فایل‌های باز چه ارتباطی با درخواست‌های شبکه دارد؟
```

2. Database Sharding and Scaling with Vitess

```markdown
# آزمایش شاردینگ پایگاه داده با Vitess

## اهداف
- آشنایی با مفهوم شاردینگ در پایگاه داده
- یادگیری نحوه مقیاس‌سازی پایگاه داده با Vitess

## نیازمندی‌ها
- Docker
- MySQL
- Go programming language (مقدماتی)

## مراحل آزمایش

1. نصب و راه‌اندازی Vitess
```bash
git clone https://github.com/vitessio/vitess.git
cd vitess
make build
```

2. پیکربندی یک پایگاه داده با چندین شارد
3. انجام عملیات CRUD با استفاده از Vitess
4. بررسی توزیع داده‌ها در شاردها

## پروژه عملی
- ایجاد یک سیستم مدیریت کاربران با قابلیت شاردینگ
- تست مقیاس‌پذیری با تولید داده تصادفی

## پرسش‌ها
- مزایا و معایب شاردینگ چیست؟
- چه زمانی از شاردینگ استفاده می‌کنید؟
```

3. Microservice Architecture Migration

```markdown
# آزمایش مهاجرت به معماری میکروسرویس

## اهداف
- درک معماری میکروسرویس
- یادگیری مهاجرت از معماری مونولیتیک به میکروسرویس

## نیازمندی‌ها
- Go programming language
- Docker
- Docker Compose
- Git

## مراحل آزمایش

1. ایجاد یک برنامه مونولیتیک ساده
2. تقسیم برنامه به سرویس‌های مستقل
3. Dockerize کردن هر سرویس
4. پیکربندی Docker Compose
5. اضافه کردن Load Balancer

## پروژه پیشنهادی
- سیستم مدیریت فروشگاه آنلاین
  - سرویس کاربران
  - سرویس محصولات
  - سرویس سفارشات
  - سرویس احراز هویت

## پرسش‌ها
- چه مزایایی در معماری میکروسرویس می‌بینید؟
- چالش‌های اصلی این معماری چیست؟
```

4. Performance Optimization by Changing Programming Language

```markdown
# آزمایش بهینه‌سازی عملکرد با تغییر زبان برنامه‌نویسی

## اهداف
- مقایسه عملکرد زبان‌های برنامه‌نویسی
- درک تأثیر انتخاب زبان در کارایی

## نیازمندی‌ها
- PHP
- Go
- Python
- کامپیوتر با منابع کافی برای تست

## آزمایش عملی

1. پیاده‌سازی یک الگوریتم پیچیده در سه زبان
   - محاسبه عدد فیبوناچی
   - پردازش تصویر
   - پردازش داده‌های حجیم

2. ابزارهای سنجش عملکرد
   - زمان اجرا
   - مصرف حافظه
   - استفاده از CPU

3. مقایسه و تحلیل نتایج

## پرسش‌ها
- چه تفاوت‌هایی در عملکرد مشاهده کردید؟
- چه عواملی در تفاوت کارایی زبان‌ها مؤثر است؟
```

These experiments capture the key technical learning scenarios from the blog post, providing hands-on educational experiences that mirror the technical challenges and solutions described in the Quizz of Kings technical evolution story.

Each experiment includes:
- Clear learning objectives
- Prerequisites
- Practical steps
- A project to implement
- Reflection questions

The experiments are designed to be educational, practical, and aligned with real-world technical challenges in software development and infrastructure scaling.