<template>
  <div>
    <div id="wish" class="about-box" style="padding-bottom: 0">
      <div class="about-a1">
        <div class="container">
          <div class="row">
            <div class="col-lg-12">
              <div class="title-box">
                <h2>Online Yılbaşı Çekilişi</h2>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-lg-12 col-md-12 col-sm-12">
              <div class="row align-items-center about-main-info">
                <div class="col-lg-6 col-md-6 col-sm-12 text_align_center">
                  <div class="full">
                    <img
                      class="img-responsive"
                      src="src/assets/img/w1.png"
                      alt="#"
                    />
                  </div>
                </div>

                <div class="col-lg-6 col-md-6 col-sm-12">
                  <h2>
                    <img
                      style="width: 60px"
                      src="src/assets/img//head_s.png"
                      alt="#"
                    />
                    Christmas is soon!
                  </h2>
                  <p>
                    Yeni yıla arkadaşlarıyla birlikte keyifli bir şekilde girmek
                    ve hediyeleşmek isteyenler hemen kağıt kaleme sarılır.
                    İsimler yazılır, torbaya atılır ve çekiliş yapılır. İsmi
                    eşleşenler birbirlerine hediye alır.
                  </p>
                  <p>
                    Yılbaşının en keyifli yanlarından biri de bu tür küçük
                    oyunlardır. Yılbaşı hediye çekilişini yilbasicekilisi.tech
                    üzerinden kolayca organize edebilir, eşleşme sonucunu
                    herkesin mail adresine gönderebilirsin.
                  </p>
                  <create-modal></create-modal>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div
        class="about-a1"
        style="
          background: #f7f7f7;
          margin-top: 50px;
          padding-top: 75px;
          padding-bottom: 50px;
        "
      >
        <div class="container">
          <div class="row">
            <div class="col-lg-12 col-md-12 col-sm-12">
              <div class="row align-items-center about-main-info">
                <div class="col-lg-6 col-md-6 col-sm-12">
                  <h2>
                    <img
                      style="width: 60px"
                      src="src/assets/img/head_s.png"
                      alt="#"
                    />
                    Geliştiriciler Hakkında
                  </h2>
                  <p>
                    Projeyi
                    <span
                      onclick="window.open('https://twitter.com/selametsamli')"
                      >Selamet Şamlı</span
                    >
                    ve
                    <span
                      onclick="window.open('https://twitter.com/ilteriskeskin')"
                      >Ali İlteriş Keskin</span
                    >
                    haftasonu projesi olarak geliştirmiştir. Proje açık
                    kaynaktır ve isteyen herkes bu projeye katkıda bulunabilir.
                  </p>
                  <p>
                    Eğer yılbaşı çekilişinde bize de hediye almak isterseniz
                    aşağıdaki bağlantılardan hediyenizi gönderebilirsiniz :)
                  </p>
                  <a
                    href="https://github.com/selamet/online-yilbasi-cekilisi/"
                    target="_blank"
                    class="hvr-radial-out button-theme"
                    >GitHub</a
                  >

                  <a
                    href="https://kreosus.com/yilbasicekilisi"
                    target="_blank"
                    class="hvr-radial-out button-theme"
                    >Bize de Hediye Al :)</a
                  >
                </div>

                <div class="col-lg-6 col-md-6 col-sm-12 text_align_center">
                  <div class="full">
                    <img
                      class="img-responsive"
                      src="src/assets/img/w2.png"
                      alt="#"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import CreateModal from "./CreateModal";

export default {
  name: "app",
  components: {
    CreateModal,
  },
  data() {
    return {
      canBeShown: false,
    };
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Poppins:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i");
@import url("https://fonts.googleapis.com/css?family=Montserrat:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i");
@import url("https://fonts.googleapis.com/css?family=Great+Vibes");

.tooltip__wave span {
  position: absolute;
  left: -100%;
  width: 200%;
  height: 100%;
  /*	background: url(src/assets/img/wave.svg) repeat-x center center;*/
  background-size: 50% auto;
}

.about-box {
  padding: 70px 0px;
}

.title-box {
  text-align: center;
  margin-bottom: 30px;
}

.title-box h2 {
  font-size: 75px;
  font-family: "Great Vibes", cursive;
  color: #e91327;
  font-weight: 400;
  padding: 0;
}

.title-box h2 span {
  color: #70c6eb;
  text-decoration: underline;
}

.about-main-info h2 span {
  color: #70c6eb;
  text-decoration: underline;
}

.about-main-info {
  margin-bottom: 30px;
}

.about-img img {
  border-radius: 10px;
}

.about-m ul {
  display: block;
  text-align: center;
  padding-bottom: 30px;
}

.about-m ul li {
  display: inline-block;
  text-align: center;
}

.about-m ul li a {
  background: #528780;
  color: #ffffff;
  width: 38px;
  height: 38px;
  text-align: center;
  line-height: 38px;
  display: block;
  border-radius: 50px;
  margin: 0px 5px;
}

.about-m ul li a:hover {
  background: #333333;
  color: #ffffff;
}

.about-main-info h2 {
  font-size: 45px;
  color: #e91327;
  font-weight: 600;
}

/* .about-main-info a {
  border-radius: 2px;
  transition: 0.2s;
  padding: 10px 25px;
  background: #e91327;
  color: #ffffff;
  font-weight: 300;
  font-size: 15px;
  border-radius: 0 15px;
  margin-top: 10px;
} */

.about-main-info a:hover {
  color: #ffffff;
}

.about-main-info div.full > img {
  height: 500px;
}

.hvr-radial-out {
  display: inline-block;
  vertical-align: middle;
  -webkit-transform: perspective(1px) translateZ(0);
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
  position: relative;
  overflow: hidden;
  background: #e1e1e1;
  -webkit-transition-property: color;
  transition-property: color;
  -webkit-transition-duration: 0.3s;
  transition-duration: 0.3s;
}

.hvr-radial-out::before {
  content: "";
  position: absolute;
  z-index: -1;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: #3a4149;
  border-radius: 100%;
  -webkit-transform: scale(0);
  transform: scale(0);
  -webkit-transition-property: transform;
  transition-property: transform;
  -webkit-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -webkit-transition-timing-function: ease-out;
  transition-timing-function: ease-out;
}

.hvr-radial-out:hover::before,
.hvr-radial-out:focus::before,
.hvr-radial-out:active::before {
  -webkit-transform: scale(2);
  transform: scale(2);
}

span {
  color: #e91327;
  cursor: pointer;
}
</style>
