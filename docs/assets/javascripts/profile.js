(function () {
  if (window.mermaid) window.mermaid.initialize({ startOnLoad: true });
  const baseButtons = Array.from(document.querySelectorAll("[data-game]"));
  const originalButton = document.querySelector("[data-extension='']");
  const extensionButton = document.querySelector("[data-extension-toggle]");
  const languageButtons = Array.from(document.querySelectorAll("[data-language-toggle]"));
  const status = document.querySelector(".profile-status");
  const profileBar = document.querySelector("#environment-profile");
  const extensionRoots = {
    "rgon": { language: "zh", root: "/rgon/zh/" },
    "rgon+": { language: "en", root: "/rgon-plus/en/" },
  };
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

  function profilePath(language, extension) {
    return extensionRoots[extension] ? extensionRoots[extension].root : `/${language}/`;
  }

  function currentProfileRoot() {
    return Object.values(extensionRoots).map((extension) => extension.root).find(
      (root) => window.location.pathname.startsWith(root)
    ) || ["/en/", "/zh/"].find((root) => window.location.pathname.startsWith(root));
  }

  function profileUrl(root, page = "") {
    const url = new URL(`${root}${page}`, window.location.origin);
    url.searchParams.set("game", profile.game);
    if (profile.extension) url.searchParams.set("extension", profile.extension);
    url.hash = window.location.hash;
    return url;
  }

  function navigateToProfile(language = currentLanguage()) {
    const root = profilePath(language, profile.extension);
    const currentRoot = currentProfileRoot();
    const page = currentRoot ? window.location.pathname.slice(currentRoot.length) : "";
    const target = profileUrl(root, page);
    if (!page || target.pathname === window.location.pathname) {
      window.location.assign(target.toString());
      return;
    }
    fetch(target.pathname, { method: "HEAD" })
      .then((response) => window.location.assign(response.ok ? target.toString() : profileUrl(root).toString()))
      .catch(() => window.location.assign(profileUrl(root).toString()));
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

  function gamesForBadge(badge) {
    if (badge.classList.contains("alldlc")) return ["all-dlcs"];
    if (badge.classList.contains("reporplus")) return ["rep", "rep+"];
    if (badge.classList.contains("repplus")) return ["rep+"];
    if (badge.classList.contains("rep") || badge.classList.contains("abrep")) return ["rep"];
    if (badge.classList.contains("abp")) return ["legacy"];
    return null;
  }

  function versionBadge(block) {
    return Array.from(block.querySelectorAll("a.badge")).find(gamesForBadge);
  }

  function annotateUpstreamEntries() {
    document.querySelectorAll("p").forEach((markerBlock) => {
      const badge = versionBadge(markerBlock);
      if (!badge || markerBlock.dataset.compatibilityAnnotated) return;
      const games = gamesForBadge(badge);
      for (let node = markerBlock; node; node = node.nextElementSibling) {
        if (node !== markerBlock && (node.matches("h3") || versionBadge(node))) break;
        node.classList.add("api-entry");
        node.dataset.games = games.join(" ");
        node.dataset.compatibilityAnnotated = "true";
      }
    });
  }

  function applyCompatibility() {
    document.querySelectorAll(".api-entry[data-games]").forEach((entry) => {
      const games = entry.dataset.games.split(" ");
      const extension = entry.dataset.extension || "";
      const baseMatches = games.includes("all-dlcs") || games.includes(profile.game);
      entry.classList.toggle("is-unavailable", !baseMatches || extension !== profile.extension);
    });
  }

  function renderSourceNotice() {
    const extensionRoot = extensionRoots[profile.extension];
    let notice = document.querySelector(".profile-source-notice");
    if (!extensionRoot) {
      if (notice) notice.remove();
      return;
    }
    if (!notice) {
      notice = document.createElement("span");
      notice.className = "profile-source-notice";
      notice.setAttribute("role", "status");
      profileBar.append(notice);
    }
    notice.textContent = extensionRoot.language === "zh"
      ? "RGON 扩展文档仅提供中文源快照。"
      : "RGON+ extension documentation is available from its English source snapshot.";
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
    renderSourceNotice();
    saveProfile();
    applyCompatibility();
  }

  baseButtons.forEach((button) => button.addEventListener("click", () => {
    profile.game = button.dataset.game;
    render();
    if (profile.extension) navigateToProfile();
  }));
  originalButton.addEventListener("click", () => {
    profile.extension = "";
    render();
  });
  extensionButton.addEventListener("click", () => {
    profile.extension = profile.extension ? "" : extensionButton.dataset.extensionToggle;
    render();
    navigateToProfile();
  });
  languageButtons.forEach((button) => button.addEventListener("click", () => {
    const language = button.dataset.languageToggle;
    localStorage.setItem("isaac-wiki-language", language);
    navigateToProfile(language);
  }));
  annotateUpstreamEntries();
  render();
  if (profile.extension && currentProfileRoot() !== profilePath(currentLanguage(), profile.extension)) {
    navigateToProfile();
  }
}());
