(function () {
  const game = document.getElementById("profile-game");
  const rgon = document.getElementById("profile-rgon");
  const rgonPlus = document.getElementById("profile-rgon-plus");
  const eid = document.getElementById("profile-eid");
  if (!game) return;

  const restore = () => {
    game.value = localStorage.getItem("isaac-wiki-game") || "rep";
    eid.checked = localStorage.getItem("isaac-wiki-eid") === "true";
    rgon.checked = localStorage.getItem("isaac-wiki-rgon") === "true";
    rgonPlus.checked = localStorage.getItem("isaac-wiki-rgon-plus") === "true";
    constrain();
  };
  const constrain = () => {
    const isRep = game.value === "rep";
    rgon.disabled = !isRep;
    rgonPlus.disabled = isRep;
    if (!isRep) rgon.checked = false;
    if (isRep) rgonPlus.checked = false;
    localStorage.setItem("isaac-wiki-game", game.value);
    localStorage.setItem("isaac-wiki-rgon", rgon.checked);
    localStorage.setItem("isaac-wiki-rgon-plus", rgonPlus.checked);
    localStorage.setItem("isaac-wiki-eid", eid.checked);
  };
  [game, rgon, rgonPlus, eid].forEach((control) => control.addEventListener("change", constrain));
  document.querySelectorAll("[data-language-toggle]").forEach((button) => {
    button.addEventListener("click", () => {
      const language = button.dataset.languageToggle;
      localStorage.setItem("isaac-wiki-language", language);
      const url = new URL(window.location.href);
      url.pathname = url.pathname.replace(/\/(en|zh)\//, `/${language}/`);
      window.location.assign(url.toString());
    });
  });
  restore();
}());
