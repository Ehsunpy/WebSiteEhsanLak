from datetime import datetime


def site_identity(request):
    """Expose personal branding + contact info globally."""
    return {
        "site_owner": {
            "name": "احسان لک",
            "tagline": "برنامه‌نویس و پژوهشگر هوش مصنوعی",
            "headline": "خلق تجربه‌های دیجیتال هوشمند و الهام‌بخش",
        },
        "contact_info": {
            "phone": "+989370546885",
            "email": "ehsanlak279@gmail.com",
            "github": "https://github.com/Ehsunpy",
            "location": "تهران، ایران",
            "year": datetime.now().year,
        },
    }

