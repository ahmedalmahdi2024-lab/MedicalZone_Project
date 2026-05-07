document
  .querySelector(".contact-form")
  .addEventListener("submit", function (e) {
    e.preventDefault();

    // 1. جلب البيانات
    const hospital = this.querySelectorAll("input")[0].value;
    const device = this.querySelectorAll("input")[1].value;
    const phone = this.querySelectorAll("input")[2].value;
    const issue = this.querySelector("textarea").value;

    // 2. تنسيق الرسالة
    const message =
      `*طلب صيانة جديد (Medical Zone)*%0A%0A` +
      `*الجهة:* ${hospital}%0A` +
      `*الجهاز:* ${device}%0A` +
      `*الهاتف:* ${phone}%0A` +
      `*العطل:* ${issue}`;

    // 3. الإرسال
    const whatsappNumber = "201153791474";
    const url = `https://wa.me/${whatsappNumber}?text=${message}`;

    window.open(url, "_blank");
  });
