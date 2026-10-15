setInterval(() => {
  fetch("sample.json").then(response => response.json()).catch(() => {});
}, 400);
