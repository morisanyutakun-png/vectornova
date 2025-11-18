from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)


# TOPページ
@app.route("/")
def index():
    return render_template("index.html")

# 料金プラン
@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

# 利用ポリシー
@app.route("/policy")
def policy():
    return render_template("policy.html")

# 質問・添削ページ
@app.route("/qanda")
def qanda():
    return render_template("qanda.html")

# ビジネスラインへ飛ぶリンク
@app.route("/business-line")
def business_line():
    return redirect("https://lin.ee/RR8PCTI")  # 実際のURLに置き換え


@app.route("/policy-for-line")
def policy_for_line():
    return render_template("policy_for_line.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)