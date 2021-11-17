# smsir

smsir is a Python library for using SMS web services (www.sms.ir)

All web service [documentation](https://apidocs.sms.ir/) is implemented

اس ام اس ای ار یک کتابخانه پایتون برای استفاده از خدمات وب سروریس اس ام اس دات ای ار است

تمامی مستند های موجود در وب سرویس پیاده سازی شده است

[مستند ها سایت](https://apidocs.sms.ir/)

## Installation

Use the package manager [pip](https://pypi.org/project/smsir/) to install smsir.

```bash
pip install smsir
```

## Usage

دریافت توکن

GET Token

```python
from smsir.token import get_token


# returns 'TOKEN'
get_token(UserApiKey='', SecretKey='')
```


دریافت اعتبار

GET credit
```python
from smsir.token import get_credit

# returns 'credit'
get_credit(token='')
```


ارسال پیام به شماره

SendByMobileNumber

```python
from smsir.sms import send_by_mobile_number

# returns 'sms response'
send_by_mobile_number(Messages='text', MobileNumbers='09XX', LineNumber='3000XXX', Token='GET Token')

```

ارسال پیام کد تایید

Send VerificationCode

```python
from smsir.sms import VerificationCode

# returns 'sms response'
VerificationCode(Code='code', MobileNumber='09XX', Token='GET Token')

```

ارسال پیام فوق سریع

send UltraFast

```python
from smsir.sms import UltraFastSend

# returns 'sms response'
parameter_array = [
    {"Parameter": "Parameters1", "ParameterValue": "Value1"},
    {"Parameter": "Parameters2", "ParameterValue": "Value2"}
]
UltraFastSend(ParameterArray=parameter_array, TemplateId='', Token='GET Token')

```

## License

[MIT](https://github.com/rahimaee/smsir/blob/main/LICENSE)