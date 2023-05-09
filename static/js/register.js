function bindEmailCaptchaClick() {
    $("#captcha-btn").click(function (event) {
        // $this：代表的是当前按钮的jquery对象
        var $this = $(this);
        // 阻止默认的事件
        event.preventDefault();
        var email = $("input[name='email']").val();
        $.ajax({
            // 默认为当前网页http://127.0.0.1:5000
            // /auth/captcha/email?email=xx@qq.com
            url: "/auth/captcha/email?email=" + email,
            method: "GET",
            success: function (result) {
                var code = result['code'];
                if (code == 200) {
                    var countdown = 5;
                    // 开始倒计时之前，就取消按钮点击事件
                    $this.off("click");
                    var timer = setInterval(function () {
                        $this.text(countdown);
                        countdown -= 1;
                        if (countdown <= 0) {
                            // 清掉定时器
                            clearInterval(timer);
                            $this.text("获取验证码");
                            // 倒计时结束重新绑定点击事件
                            bindEmailCaptchaClick();
                        }
                    }, 1000);
                    // alert("邮箱发送成功！");
                } else {
                    alert(result['message']);
                }
            },
            fail: function (error) {
                console.log(error);
            }
        })
    });
}


// 整个网页都加载完毕后再执行的，$是jquery的缩写
$(function () {
    bindEmailCaptchaClick();
});