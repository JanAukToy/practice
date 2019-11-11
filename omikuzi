
const today = new Date();       //時間取得

const time = today.getHours();

if (time > 4 && time < 12) {
  console.log("おはようございます。");
} else if (time > 11 && time < 18) {
  console.log("こんにちは。");
} else {
  console.log("こんばんは。");
};

console.log("おみくじ起動します。")

const seconds = today.getSeconds();         //2桁
const mseconds = today.getMilliseconds();   //3桁

const min = 1;      //ランダムナンバー最小値
const max = 100;    //ランダムナンバー最大値

const xnumber = Math.floor(Math.random() * (max + 1 - min)) + min;

if (xnumber % 3 > 1) {
  if (seconds % 3 > 1) {
    if (mseconds % 3 > 1) {
      console.log("おめでとうございます。大吉です。");
    } else {
      console.log("微妙です。小吉です。");
    };
  } else {
    console.log("出直して下さい。凶です。");
  };
} else {
  if (seconds % 3 > 1) {
    if (mseconds % 3 > 1) {
      console.log("もう少しでしたね。中吉です。");
    } else {
      console.log("残念。末吉です。");
    };
  } else {
    console.log("大凶です。トイレ掃除へ行きましょう。");
  };
};
