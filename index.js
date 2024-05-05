const express = require("express");
const router = require("./routes/start");
const cors = require("cors");
const app = express();
const port = 3000;

app.use(express.json());
app.use(router);
app.use(cors());

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});

const express = require("express");
const ip = require("ip");
const bodyParser = require("body-parser");

const ip = express();
const ipAddr = ip.address();
let lastHouseVisited = "";

app.use(bodyParser.json());

app.get("/", (req, res) => {
  res.json({ message: lastHouseVisited });
});

app.post("/", (req, res) => {
  console.log(req.body);
  lastHouseVisited = req.body.house;
  res.json({ message: lastHouseVisited });
});

app.listen(4000, () => {
  console.log("Server running at: http://" + ipAddr + ":4000");
});
