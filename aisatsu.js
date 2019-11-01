
/*日付取得→時間取得*/
const today = new Date();

const time = today.getHours();

if (time>4 && time<12) {
  console.log("おはようございます");
} else if (time>11 && time<18) {
  console.log("こんにちは");
}else {
  console.log("こんばんは");
};
