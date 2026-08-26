(function () {
  if (window.mermaid) window.mermaid.initialize({ startOnLoad: true });
  const baseButtons = Array.from(document.querySelectorAll("[data-game]"));
  const originalButton = document.querySelector("[data-extension='']");
  const extensionButton = document.querySelector("[data-extension-toggle]");
  const languageButtons = Array.from(document.querySelectorAll("[data-language-toggle]"));
  const profileBar = document.querySelector("#environment-profile");
  if (!baseButtons.length || !originalButton || !extensionButton) return;

  const query = new URLSearchParams(window.location.search);
  const profile = {
    game: query.get("game") || localStorage.getItem("isaac-wiki-game") || "rep",
    extension: query.get("extension") || localStorage.getItem("isaac-wiki-extension") || "",
  };

  function normalizeProfile() {
    if (profile.game !== "rep" && profile.game !== "rep+") profile.game = "rep";
    if (profile.extension !== "rgon") profile.extension = "";
  }

  function currentLanguage() {
    return /\/zh(?:\/|$)/.test(window.location.pathname) ? "zh" : "en";
  }

  function siteBasePath() {
    const match = window.location.pathname.match(/^(.*?)(?:\/en|\/zh)(?:\/|$)/);
    return match && match[1] ? `${match[1]}/` : "/";
  }

  function profilePath(language) {
    return `${siteBasePath()}${language}/`;
  }

  function profileUrl(root, page = "") {
    const url = new URL(`${root}${page}`, window.location.origin);
    url.searchParams.set("game", profile.game);
    if (profile.extension) url.searchParams.set("extension", profile.extension);
    url.hash = window.location.hash;
    return url;
  }

  function navigateToLanguage(language) {
    const root = profilePath(language);
    const currentRoot = profilePath(currentLanguage());
    const page = window.location.pathname.startsWith(currentRoot)
      ? window.location.pathname.slice(currentRoot.length)
      : "";
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
      const signature = markerBlock.nextElementSibling;
      if (!signature || !signature.matches("h4")) return;
      signature.append(" ", badge);
      signature.classList.add("api-signature");
      signature.dataset.games = games.join(" ");
      markerBlock.dataset.compatibilityAnnotated = "true";
      markerBlock.remove();
    });
    document.querySelectorAll("h4.copyable, h4:has(a.badge)").forEach((signature) => {
      signature.classList.add("api-signature");
    });
  }

  function applyCompatibility() {
    document.querySelectorAll(".api-signature[data-games]").forEach((entry) => {
      const games = entry.dataset.games.split(" ");
      const baseMatches = games.includes("all-dlcs") || games.includes(profile.game);
      entry.classList.toggle("is-unavailable", !baseMatches);
    });
  }

  function applyExtensionVisibility() {
    const enabled = profile.extension === "rgon";
    document.querySelectorAll(".rgon-extension, .rgon-only").forEach((block) => {
      block.toggleAttribute("hidden", !enabled);
      block.setAttribute("aria-hidden", String(!enabled));
      block.classList.toggle("is-visible", enabled);
    });
    document.querySelectorAll(".rgon-toc-entry").forEach((entry) => {
      const isOnly = entry.classList.contains("rgon-toc-only");
      entry.toggleAttribute("hidden", isOnly && !enabled);
      entry.classList.toggle("is-rgon-active", enabled);
    });
  }

  function hasFollowingExtension(heading) {
    for (let sibling = heading.nextElementSibling; sibling; sibling = sibling.nextElementSibling) {
      if (sibling.matches("h2, h3")) return false;
      if (sibling.classList.contains("rgon-extension")) return true;
    }
    return false;
  }

  function annotateExtensionToc() {
    const extensionEntries = [];
    document.querySelectorAll(".md-sidebar--secondary a[href^='#']").forEach((link) => {
      const id = decodeURIComponent(link.hash.slice(1));
      const target = document.getElementById(id);
      if (!target) return;
      const entry = link.closest("li.md-nav__item");
      if (!entry) return;
      const inOnlyBlock = Boolean(target.closest(".rgon-only"));
      if (!inOnlyBlock && !hasFollowingExtension(target)) return;
      entry.classList.add("rgon-toc-entry");
      if (inOnlyBlock) {
        entry.classList.add("rgon-toc-only");
        extensionEntries.push(entry);
      }
    });
    if (extensionEntries.length) extensionEntries[0].classList.add("is-first");
  }

  function enablePrimarySectionToggles() {
    document.querySelectorAll(".md-sidebar--primary li.md-nav__item--nested").forEach((item) => {
      const nestedNav = item.querySelector(":scope > nav.md-nav[data-md-level='2']");
      const toggle = item.querySelector(":scope > input.md-nav__toggle[type='checkbox']");
      const label = item.querySelector(":scope > label[for]");
      if (!nestedNav || !toggle || !label) return;
      item.classList.remove("md-nav__item--section");
      label.tabIndex = 0;
      label.setAttribute("role", "button");
      const updateAria = () => label.setAttribute("aria-expanded", String(toggle.checked));
      updateAria();
      toggle.addEventListener("change", updateAria);
      label.addEventListener("keydown", (event) => {
        if (event.key !== "Enter" && event.key !== " ") return;
        event.preventDefault();
        toggle.checked = !toggle.checked;
        toggle.dispatchEvent(new Event("change", { bubbles: true }));
      });
    });
  }

  function rewriteProfileNavigation() {
    const targetRoot = profilePath(currentLanguage());
    const originalRoot = profilePath("en");
    document.querySelectorAll(".md-nav a[href]").forEach((link) => {
      const url = new URL(link.href, window.location.origin);
      if (url.origin !== window.location.origin || !url.pathname.startsWith(originalRoot)) return;
      const target = profileUrl(targetRoot, url.pathname.slice(originalRoot.length));
      target.hash = url.hash;
      link.href = target.toString();
    });
  }

  function syncNavigationState() {
    const currentPath = window.location.pathname.replace(/\/+$/, "/");
    document.querySelectorAll(".md-sidebar--primary a.md-nav__link").forEach((link) => {
      const linkPath = new URL(link.href, window.location.origin).pathname.replace(/\/+$/, "/");
      if (linkPath !== currentPath) return;
      link.classList.add("md-nav__link--active");
      const item = link.closest("li.md-nav__item");
      if (item) item.classList.add("md-nav__item--active");
      for (let nav = link.closest("nav.md-nav"); nav; nav = nav.parentElement?.closest("nav.md-nav")) {
        const item = nav.parentElement;
        if (!item) continue;
        item.classList.add("md-nav__item--active");
        const toggle = item.querySelector(":scope > input.md-nav__toggle[type='checkbox']");
        if (toggle) {
          toggle.checked = true;
          nav.setAttribute("aria-expanded", "true");
        }
      }
    });
  }

  function render() {
    normalizeProfile();
    const activeExtension = profile.extension === "rgon";
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
    profileBar.classList.toggle("is-rgon", activeExtension);
    saveProfile();
    applyCompatibility();
    applyExtensionVisibility();
    rewriteProfileNavigation();
    syncNavigationState();
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
    profile.extension = profile.extension ? "" : "rgon";
    render();
  });
  languageButtons.forEach((button) => button.addEventListener("click", () => {
    localStorage.setItem("isaac-wiki-language", button.dataset.languageToggle);
    navigateToLanguage(button.dataset.languageToggle);
  }));
  annotateUpstreamEntries();
  annotateExtensionToc();
  enablePrimarySectionToggles();
  render();
}());
