<template>
  <div>
    <a href="#" @click.prevent="show" class="hvr-radial-out button-theme draw-button"
    >Çekiliş Yap!</a
    >
    <modal
      name="create-modal"
      :min-width="200"
      :min-height="200"
      :scrollable="true"
      :reset="true"
      :width="screenWidth"
      height="auto"
    >
      <div class="header">
        <h4>Mutlu Yıllar...</h4>
      </div>

      <div style="margin-top: 10px" class="participants">
        <div
          class="participants-form-list"
          v-for="(participant, index) in participants"
          :key="index"
        >
          <div class="participant-form">

            <div class="default-form">
              <input
                v-model="participant.name"
                type="text"
                name="name"
                placeholder="Katılımcı Adı"
                class="nameInput"
              />
              <input
                v-model="participant.email"
                type="text"
                name="email"
                placeholder="E-posta"
                class="nameInput"
              />
              <button
                class="remove-participant"
                style="cursor: pointer;"
                @click="removeParticipant(index)"
              >
                <span>Sil</span>
                <span>x</span>
              </button>
            </div>
            <div class="form-with-address">
              <textarea
                class="nameInput text-area"
                v-if="addressStatus"
                v-model="participant.address"
                name="address"
                placeholder="Adres"
              />
            </div>
          </div>
          <span class="list-fix"></span>
        </div>
      </div>
      <div class="footer">
        <div class="add-address">
          <div class="add-address-btn">
            <button
              :class  ="[{'active-class' : addressStatus}, 'add-address-btn-item']" 
              @click  ="selectAddAddress(true)">
               + Adres Bilgisi Ekle
            </button>
            <button
              :class  ="[{'active-class' : !addressStatus}, 'add-address-btn-item']" 
              @click  ="selectAddAddress(false)">
              Adres Bilgisi Ekleme
            </button>
          </div>
        </div>
        <div class="add-participant">
          <a
            href="#"
            @click="addParticipant()"
          >+ Katılımcı Ekle</a
          >
        </div>
        <div class="buttons">
          <a href="#" @click="createDraw()" class="hvr-radial-out button-theme start-draw"
          >Çekilişi Yap!</a
          >
        </div>

        <p class="info-text">
          Eşleşmeler her bir katılımcının
          mail adresine gönderilecektir.
        </p>
        <div style="height: 10px">

        </div>
      </div>
    </modal>
    <modal
      name="finally-modal"
      :min-width="200"
      :min-height="200"
      :scrollable="true"
      :reset="true"
      :width="screenWidth"
      height="auto"
    >
      <div class="header">
        <h4>Mutlu Yıllar...</h4>
      </div>

      <div style="margin-top: 10px" class="finally-content">
        <p>Tebrikler yılbaşı çekilişiniz başarı ile gerçekleşti. Lütfen mail kutunuzu kontrol ediniz. <br> <small>(Spam
          kutunuzu kontrol etmeyi unutmayınız :)</small></p>
        <img src="src/assets/img/gift.png" alt="" height="60%" width="60%">

        <p>2021 yılında neşeniz, sağlığınız, mutluluğuz ve huzurunuz eksik olmasın. Mutlu yıllar dileriz.</p>
        <p class="logos">

          <span
            onclick="window.open('https://github.com/selamet/online-yilbasi-cekilisi')"
          ><i class="fab fa-github"></i></span>

          <span
            onclick="window.open('mailto:yeniyilcekilisi@gmail.com')"
          ><i class="fas fa-envelope"></i></span>
          <span
            onclick="window.open('https://kreosus.com/yilbasicekilisi')"
          ><i class="fas fa-gift"></i></span>

        </p>

      </div>
      <div class="last-message">
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
          Eğer yılbaşı bize de hediye almak isterseniz <span
          onclick="window.open('https://twitter.com/ilteriskeskin')"
        >buradan </span> gönderebilirsiniz :)<br>

        </p>
      </div>
    </modal>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      screenWidth: '',
      participants: [{id: 1, name: "", email: ""}],
      mailCheck: true,
      addressStatus: false,
    };
  },
  created() {
    console.log(screen.width)
    if (screen.width < 750) {
      this.screenWidth = "90%"
    } else {
      this.screenWidth = "60%"
    }
  },
  methods: {
    show() {
      this.$modal.show("create-modal");
    },
    hide() {
      this.$modal.hide("create-modal");
    },
    showFinally() {
      this.$modal.show("finally-modal");
    },
    hideFinally() {
      this.$modal.hide("finally-modal");
    },
    addParticipant() {
      let id = this.participants.length + 1;
      if (!this.addressStatus) {
        this.participants.push({
          id: id,
          name: "",
          email: "",
        });
      } else {
        this.participants.push({
          id: id,
          name: "",
          email: "",
          address: "",
        });
      }

    },
    removeParticipant(index) {
      this.participants.splice(index, 1);
    },
    selectAddAddress(hasAddress) {
      this.addressStatus = hasAddress;
      this.addressStatus
        ? this.participants.map(item => item.address = '')
        : this.participants.map(item => delete item.address)
    },
    findEmptyField() {
      const reg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
      let arr = this.participants.filter(function (a) {
        if (!reg.test(a.email) && a.email !== "") {
          alert(`${a.email} Geçerli bir eposta adresi olarak gözükmüyor.`)
          this.mailCheck = false;
        }
        if (!(a.name === "" || a.email === "")) {
          return a;
        }
      });
      return arr;
    },
    createDraw() {
      this.mailCheck = true;
      let arr = this.findEmptyField();
      if (arr && arr.length > 1 && this.mailCheck) {
        axios.post("http://127.0.0.1:5000", arr).then((response) => {
          this.hide();
          this.showFinally();
          this.addressStatus = false;
          this.participants = [{id: 1, name: "", email: ""}];
        });
      } else if (arr.length === 0) {
        alert("Lütfen Tüm alanları doldurun")
      } else if (arr.length === 1) {
        alert("Tek başına çekiliş yapamazsın :(")
      }

    },
  },

};
</script>


<style>

.active-class {
  background: #3A4149!important;
  outline: none!important;
  text-decoration: underline!important;
  color: white!important;
}

.start-draw {
  width: 80%;
  margin: 20px 0 10px 10px;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 16px;
  background: #38c172;
  color: white;
  font-weight: 600;
  letter-spacing: 1px;
  border-radius: 4px;
  height: 60px;
}

.draw-button {
  width: 100%;
  border: none;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 15px 0;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 900;
  letter-spacing: 1px;
  background: #e91327;
  color: white;
}

.nameInput {
  border: 1px solid lightgray;
  width: 40%;
  margin: 0;
  padding: 5px 10px;
  height: 50px;
  border-radius: 4px;
  color: #3A4149;
  background: #f4f7fa;
}

.text-area {
  width: 100%;
  display: flex;
  height: auto;
  margin: 20px;
  width: 100%;
}

.default-form {
  display: flex;
  width: 100%;
  align-items: center;
  justify-content: space-between;
  margin: 0 20px 0 10px;
}

.form-with-address {
  width: 100%;
  display: flex;
}

.list-fix {
  display: flex;
  widows: 100%;
  height: 30px;
}

.add-address {
  /* position: absolute;
  top: 0;
  right: 0;
  height: 100px;
  display: flex;
  align-items: center; */
}

.add-address-btn {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.add-address-btn-item {
  background: #ebebeb;
  color: #3A4149;
  border: none;
  width: 90px;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: .5px;
  width: 40%;
  height: 50px;
}

.add-address-btn-item:first-child {
  border-top-left-radius: 4px;
  border-bottom-left-radius: 4px;
}

.add-address-btn-item:last-child {
  border-top-right-radius: 4px;
  border-bottom-right-radius: 4px;
}

.add-participant {
  width: auto;
  position: absolute;
  top: 0;
  right: 0;
  height: 100px;
  display: flex;
  align-items: center;
}


.add-participant a {
  border: 1px solid #666666;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
  color: #3A4149;
  padding: 5px 10px;
  margin-right: 20px;
}

.add-participant a:hover {
  color: currentColor;
}

.remove-participant {
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 4px;
  padding: 5px 10px;
  cursor: pointer;
  background: #ec5161;
  border: 1px solid white;
  height: 50px;
  border: none;
  width: 60px;
}

.remove-participant span {
  color: #fff;
  font-size: 14px;
  font-weight: 600;
}

.remove-participant span:last-child {
  padding-bottom: 2px;
  padding-left: 4px;
}

.header {
  margin: 0;
  padding: 0;
  margin-bottom: 30px;
  height: 100px;
  background-color: #fff;
  box-shadow: 0 5px 10px #f4f7fa;
  display: flex;
  justify-content: center;
  align-items: center;
}

.header h4 {
  margin-top: 10px;
  font-size: 42px;
  color: #3A4149;
  font-family: "Great Vibes", cursive;
  font-weight: 300;
}

.info-text {
  color: #3A4149;
  font-weight: 600;
  opacity: 0.8;
}

@import url(https://fonts.googleapis.com/css?family=Roboto:400,300,500);
*:focus {
  outline: none;
}

img {
  object-fit: contain;
}

body {
  margin: 0;
  padding: 0;
  background: #ddd;
  font-size: 16px;
  color: #3A4149;
  font-family: "Roboto", sans-serif;
  font-weight: 300;
}

h1 {
  margin: 0 0 20px 0;
  font-weight: 300;
  font-size: 28px;
}

.participants {
  height: 300px;
  overflow: scroll;
}

.finally-content {
  height: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;


}

.finally-content p {
  color: #222222;
  text-align: center;
}

.logos span i {
  color: #222222;
  font-size: 24px;
  margin: 0 5px 0 5px;
}


.participant-form {
  display: flex;
  flex-wrap: wrap;
  /* margin: 2px 10px 0px 10px; */
  align-items: center;
  justify-content: center;
}

.participant-form input {
  width: calc(50% - 30px);
  margin: 0 10px;
}

.last-message {
  background-color: #ddd;
  height: auto;
  display: flex;
  align-items: center;
  justify-items: center;
  flex-direction: column;
}

.last-message p {
  color: #222222;
  font-size: 13px;
  margin: 10px 10px 0 10px;
  text-align: center;
}

.footer {
  padding-top: 30px;
  background: #fff;
  height: auto;
  text-align: center;
}

.buttons {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
}

.buttons a {
  margin-right: 10px;
}

@media (max-width: 991px) {
  .add-participant {
    width: 100%;
    top: 80px;
  }
  .add-participant a {
    width: 100%;
    margin: 0 20px;
  }

  .header {
    height: 160px;
  }

  .header h4 {
    font-size: 32px;
  }

  .add-address-btn-item {
    font-size: 12px;
  }
}

</style>
