const express = require("express");
const app = express();

app.get("/run", (req, res) => {
  res.send(eval(req.query.cmd)); // SAST: Code injection
});

app.listen(3000);
