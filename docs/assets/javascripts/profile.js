(function () {
  const baseButtons = Array.from(document.querySelectorAll("[data-game]"));
  const originalButton = document.querySelector("[data-extension='']");
  const extensionButton = document.querySelector("[data-extension-toggle]");
  const languageButtons = Array.from(document.querySelectorAll("[data-language-toggle]"));
  const status = document.querySelector(".profile-status");
  if (!baseButtons.length || !originalButton || !extensionButton) return;

  const query = new URLSearchParams(window.location.search);
  const profile = {
    game: query.get("game") || localStorage.getItem("isaac-wiki-game") || "rep",
    extension: query.get("extension") || localStorage.getItem("isaac-wiki-extension") || "",
  };

  function normalizeProfile() {
    if (profile.game !== "rep" && profile.game !== "rep+") profile.game = "rep";
    if (profile.extension && profile.extension !== "rgon" && profile.extension !== "rgon+") profile.extension = "";
    if (profile.extension === "rgon" && profile.game === "rep+") profile.extension = "rgon+";
    if (profile.extension === "rgon+" && profile.game === "rep") profile.extension = "rgon";
  }

  function currentLanguage() {
    return /\/(zh)(?:\/|$)/.test(window.location.pathname) ? "zh" : "en";
  }

  function saveProfile() {
    const url = new URL(window.location.href);
    url.searchParams.set("game", profile.game);
    if (profile.extension) url.searchParams.set("extension", profile.extension);
    else url.searchParams.delete("extension");
    localStorage.setItem("isaac-wiki-game", profile.game);
    localStorage.setItem("isaac-wiki-extension", profile.extension);
    window.history.replaceState({}, "", url);
  }

  function applyCompatibility() {
    document.querySelectorAll(".api-entry[data-games]").forEach((entry) => {
      const games = entry.dataset.games.split(" ");
      const extension = entry.dataset.extension || "";
      const baseMatches = games.includes("all-dlcs") || games.includes(profile.game);
      entry.classList.toggle("is-unavailable", !baseMatches || extension !== profile.extension);
    });
  }

  function render() {
    normalizeProfile();
    const rgonLabel = profile.game === "rep+" ? "RGON+" : "RGON";
    const activeExtension = profile.extension === "rgon" || profile.extension === "rgon+";
    extensionButton.textContent = rgonLabel;
    extensionButton.dataset.extensionToggle = profile.game === "rep+" ? "rgon+" : "rgon";
    baseButtons.forEach((button) => {
      const active = button.dataset.game === profile.game;
      button.classList.toggle("is-selected", active);
      button.setAttribute("aria-pressed", String(active));
    });
    originalButton.classList.toggle("is-selected", !activeExtension);
    originalButton.setAttribute("aria-pressed", String(!activeExtension));
    extensionButton.classList.toggle("is-selected", activeExtension);
    extensionButton.setAttribute("aria-pressed", String(activeExtension));
    languageButtons.forEach((button) => {
      const active = button.dataset.languageToggle === currentLanguage();
      button.classList.toggle("is-selected", active);
      button.setAttribute("aria-pressed", String(active));
    });
    if (status) status.textContent = `${profile.game.toUpperCase()}${activeExtension ? ` + ${rgonLabel}` : ""}`;
    saveProfile();
    applyCompatibility();
  }

  baseButtons.forEach((button) => button.addEventListener("click", () => {
    profile.game = button.dataset.game;
    render();
  }));
  originalButton.addEventListener("click", () => {
    profile.extension = "";
    render();
  });
  extensionButton.addEventListener("click", () => {
    profile.extension = profile.extension ? "" : extensionButton.dataset.extensionToggle;
    render();
  });
  languageButtons.forEach((button) => button.addEventListener("click", () => {
    const url = new URL(window.location.href);
    const language = button.dataset.languageToggle;
    localStorage.setItem("isaac-wiki-language", language);
    url.pathname = /\/(en|zh)(?=\/|$)/.test(url.pathname)
      ? url.pathname.replace(/\/(en|zh)(?=\/|$)/, `/${language}`)
      : `${url.pathname.replace(/\/$/, "")}/${language}/`;
    window.location.assign(url.toString());
  }));
  render();
}());
