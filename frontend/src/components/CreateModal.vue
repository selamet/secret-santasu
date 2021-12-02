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
            <input
              class="nameInput"
              v-if="addressStatus"
              v-model="participant.address"
              type="text"
              name="address"
              placeholder="Adres"
            />
            <i
              class="glyphicon glyphicon-remove"
              style="cursor: pointer;"
              @click="removeParticipant(index)"
            ></i><br>

          </div>
          <hr>
        </div>
      </div>
      <div class="footer">
        <p>
          <span style="color: #e91327">> </span>Eşleşmeler her bir katılımcının
          mail adresine gönderilecektir.
        </p>
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
            class=""
          >Katılımcı Ekle</a
          >
        </div>
        <div class="buttons">
          <a href="#" @click="createDraw()" class="hvr-radial-out button-theme start-draw"
          >Çekilişi Yap!</a
          >
        </div>
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
  background: #ccc!important;
  outline: none!important;
  text-decoration: underline!important;
}

.start-draw {
  width: calc(80% + 20px);
  background: black;
  margin: 20px;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 18px;
  color: white;
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
  color: gray;
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
  color: gray;
  border: none;
  width: 90px;
  color: #00000090;
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
  position: absolute;
  top: 0;
  right: 0;
  height: 100px;
  display: flex;
  align-items: center;
}

.add-participant a {
  border: 1px solid white;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
  color: white;
  padding: 5px 10px;
  margin-right: 20px;
}

.header {
  margin: 0;
  padding: 0;
  height: 100px;
  background-color: #ccc;
  /* height: 60px; */
  display: flex;
  justify-content: center;
  align-items: center;
}

.header h4 {
  margin-top: 10px;
  font-size: 42px;
  color: #ffffff;
  font-family: "Great Vibes", cursive;
  font-weight: 300;
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
  color: #222;
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
  margin: 2px 10px 0px 10px;
  align-items: center;
  justify-content: center;
}

.participant-form input {
  margin: 3px 10px 0px 10px;
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
  background-color: #ddd;
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
/* 
input[type="text"],
input[type="password"] {
  display: block;
  box-sizing: border-box;
  margin-bottom: 20px;
  padding: 4px;
  width: 220px;
  height: 32px;
  border: none;
  border-bottom: 1px solid #aaa;
  font-family: "Roboto", sans-serif;
  font-weight: 400;
  font-size: 15px;
  transition: 0.2s ease;
}

input[type="text"]:focus,
input[type="password"]:focus {
  border-bottom: 2px solid #e91327;
  color: black;
  transition: 0.2s ease;
}

input[type="submit"] {
  margin-top: 28px;
  width: 120px;
  height: 32px;
  background: #e91327;
  border: none;
  border-radius: 2px;
  color: #fff;
  font-family: "Roboto", sans-serif;
  font-weight: 500;
  text-transform: uppercase;
  transition: 0.1s ease;
  cursor: pointer;
}

input[type="submit"]:hover,
input[type="submit"]:focus {
  opacity: 0.8;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
  transition: 0.1s ease;
}

input[type="submit"]:active {
  opacity: 1;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.4);
  transition: 0.1s ease;
}

@media only screen and (max-width: 755px) {
  .participant-form {
    flex-direction: column;
  }

  .participant-form input {
    width: 100%;
  }
} */


</style>
