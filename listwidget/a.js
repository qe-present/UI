var f="Hm_Iuvt_cdb524f42f0ce19b169b8072123a4727";
function m(t,e) {
     n = e.indexOf(t + "=");
  if (-1 != n) {
    n = n + t.length + 1;
    var r = e.indexOf(";", n);
    return -1 == r && (r = e.length),
      unescape(e.substring(n, r))
  }
  return null
}
function h(t, e) {
  if (null == e || e.length <= 0)
    return console.log("Please enter a password with which to encrypt the message."),
      null;
  for (var n = "", i = 0; i < e.length; i++)
    n += e.charCodeAt(i).toString();
  var r = Math.floor(n.length / 5)
    , o = parseInt(n.charAt(r) + n.charAt(2 * r) + n.charAt(3 * r) + n.charAt(4 * r) + n.charAt(5 * r))
    , l = Math.ceil(e.length / 2)
    , c = Math.pow(2, 31) - 1;
  if (o < 2)
    return console.log("Algorithm cannot find a suitable hash. Please choose a different password. \nPossible considerations are to choose a more complex or longer password."),
      null;
  var d = Math.round(1e9 * Math.random()) % 1e8;
  for (n += d; n.length > 10; )
    n = (parseInt(n.substring(0, 10)) + parseInt(n.substring(10, n.length))).toString();
  n = (o * n + l) % c;
  var h = ""
    , f = "";
  for (i = 0; i < t.length; i++)
    f += (h = parseInt(t.charCodeAt(i) ^ Math.floor(n / c * 255))) < 16 ? "0" + h.toString(16) : h.toString(16),
      n = (o * n + l) % c;
  for (d = d.toString(16); d.length < 8; )
    d = "0" + d;
  return f += d
}
function secret(cookie) {
    var t=m(f,cookie);
    return h(t,f);

}

