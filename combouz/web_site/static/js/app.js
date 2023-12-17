!function () {
    var e = {
        56: function () {
            var e = document.querySelector(".header__btn"), t = document.querySelector(".header__items"),
                r = document.querySelector(".header__abs"), n = document.querySelector(".header__close"),
                o = document.querySelector(".header__lang"), i = document.querySelector(".header__lang-options");
            if (e && t && r && n) {
                var a = function () {
                    var o = arguments.length > 0 && void 0 !== arguments[0] && arguments[0];
                    e.classList[o ? "add" : "remove"]("active"), t.classList[o ? "add" : "remove"]("active"), r.classList[o ? "add" : "remove"]("active"), n.classList[o ? "add" : "remove"]("active"), document.body.style.overflow = o ? "hidden" : ""
                };
                e.addEventListener("click", (function () {
                    a(!0)
                })), [n, r].forEach((function (e) {
                    e.addEventListener("click", (function () {
                        a()
                    }))
                }))
            }
            o && i && o.addEventListener("click", (function (e) {
                var t = i.classList.contains("show");
                i.classList[t ? "remove" : "add"]("show")
            }))
        }, 379: function (e) {
            "use strict";
            var t = [];

            function r(e) {
                for (var r = -1, n = 0; n < t.length; n++) if (t[n].identifier === e) {
                    r = n;
                    break
                }
                return r
            }

            function n(e, n) {
                for (var i = {}, a = [], s = 0; s < e.length; s++) {
                    var c = e[s], l = n.base ? c[0] + n.base : c[0], u = i[l] || 0, d = "".concat(l, " ").concat(u);
                    i[l] = u + 1;
                    var f = r(d), v = {css: c[1], media: c[2], sourceMap: c[3], supports: c[4], layer: c[5]};
                    if (-1 !== f) t[f].references++, t[f].updater(v); else {
                        var m = o(v, n);
                        n.byIndex = s, t.splice(s, 0, {identifier: d, updater: m, references: 1})
                    }
                    a.push(d)
                }
                return a
            }

            function o(e, t) {
                var r = t.domAPI(t);
                return r.update(e), function (t) {
                    if (t) {
                        if (t.css === e.css && t.media === e.media && t.sourceMap === e.sourceMap && t.supports === e.supports && t.layer === e.layer) return;
                        r.update(e = t)
                    } else r.remove()
                }
            }

            e.exports = function (e, o) {
                var i = n(e = e || [], o = o || {});
                return function (e) {
                    e = e || [];
                    for (var a = 0; a < i.length; a++) {
                        var s = r(i[a]);
                        t[s].references--
                    }
                    for (var c = n(e, o), l = 0; l < i.length; l++) {
                        var u = r(i[l]);
                        0 === t[u].references && (t[u].updater(), t.splice(u, 1))
                    }
                    i = c
                }
            }
        }, 569: function (e) {
            "use strict";
            var t = {};
            e.exports = function (e, r) {
                var n = function (e) {
                    if (void 0 === t[e]) {
                        var r = document.querySelector(e);
                        if (window.HTMLIFrameElement && r instanceof window.HTMLIFrameElement) try {
                            r = r.contentDocument.head
                        } catch (e) {
                            r = null
                        }
                        t[e] = r
                    }
                    return t[e]
                }(e);
                if (!n) throw new Error("Couldn't find a style target. This probably means that the value for the 'insert' parameter is invalid.");
                n.appendChild(r)
            }
        }, 216: function (e) {
            "use strict";
            e.exports = function (e) {
                var t = document.createElement("style");
                return e.setAttributes(t, e.attributes), e.insert(t, e.options), t
            }
        }, 565: function (e, t, r) {
            "use strict";
            e.exports = function (e) {
                var t = r.nc;
                t && e.setAttribute("nonce", t)
            }
        }, 795: function (e) {
            "use strict";
            e.exports = function (e) {
                if ("undefined" == typeof document) return {
                    update: function () {
                    }, remove: function () {
                    }
                };
                var t = e.insertStyleElement(e);
                return {
                    update: function (r) {
                        !function (e, t, r) {
                            var n = "";
                            r.supports && (n += "@supports (".concat(r.supports, ") {")), r.media && (n += "@media ".concat(r.media, " {"));
                            var o = void 0 !== r.layer;
                            o && (n += "@layer".concat(r.layer.length > 0 ? " ".concat(r.layer) : "", " {")), n += r.css, o && (n += "}"), r.media && (n += "}"), r.supports && (n += "}");
                            var i = r.sourceMap;
                            i && "undefined" != typeof btoa && (n += "\n/*# sourceMappingURL=data:application/json;base64,".concat(btoa(unescape(encodeURIComponent(JSON.stringify(i)))), " */")), t.styleTagTransform(n, e, t.options)
                        }(t, e, r)
                    }, remove: function () {
                        !function (e) {
                            if (null === e.parentNode) return !1;
                            e.parentNode.removeChild(e)
                        }(t)
                    }
                }
            }
        }, 589: function (e) {
            "use strict";
            e.exports = function (e, t) {
                if (t.styleSheet) t.styleSheet.cssText = e; else {
                    for (; t.firstChild;) t.removeChild(t.firstChild);
                    t.appendChild(document.createTextNode(e))
                }
            }
        }
    }, t = {};

    function r(n) {
        var o = t[n];
        if (void 0 !== o) return o.exports;
        var i = t[n] = {exports: {}};
        return e[n](i, i.exports, r), i.exports
    }

    r.n = function (e) {
        var t = e && e.__esModule ? function () {
            return e.default
        } : function () {
            return e
        };
        return r.d(t, {a: t}), t
    }, r.d = function (e, t) {
        for (var n in t) r.o(t, n) && !r.o(e, n) && Object.defineProperty(e, n, {enumerable: !0, get: t[n]})
    }, r.o = function (e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }, r.nc = void 0, function () {
        "use strict";
        var e = r(379), t = r.n(e), n = r(795), o = r.n(n), i = r(569), a = r.n(i), s = r(565), c = r.n(s), l = r(216),
            u = r.n(l), d = r(589), f = r.n(d), v = {};

        function m(e) {
            e.on("slideChangeTransitionStart", (function (e) {
                var t = e.activeIndex - 1, r = e.slides;
                r.forEach((function (e) {
                    e.style.transform = "", e.style.transition = ""
                })), r[t] && (r[t].style.transition = "200ms linear", r[t].style.transform = "translateY(500px)")
            }))
        }

        v.styleTagTransform = f(), v.setAttributes = c(), v.insert = a().bind(null, "head"), v.domAPI = o(), v.insertStyleElement = u(), t()({}, v);
        var p = document.querySelector(".gallery-projects__slider");
        if (p) {
            var y = new Swiper(p, {
                grabCursor: !0,
                slidesPerView: 1.2,
                width: 230,
                loop: !0,
                navigation: {nextEl: ".gallery-projects__next"},
                pagination: {
                    el: ".gallery-projects__pagination",
                    clickable: !0,
                    bulletActiveClass: "active",
                    bulletClass: "gallery-projects__bullet"
                },
                breakpoints: {1016: {width: 404}, 680: {width: 300}}
            });
            m(y), p.querySelectorAll(".gallery-projects__alternate").forEach((function (e) {
                e.addEventListener("click", (function () {
                    y.slideNext()
                }))
            }))
        }
        var h = document.querySelector(".best-curtains__slider");
        h && new Swiper(h, {grabCursor: !0, slidesPerView: 1, loop: !0});
        var _ = document.querySelector(".about__slider");
        _ && m(new Swiper(_, {
            grabCursor: !0,
            slidesPerView: 1.3,
            spaceBetween: 30,
            loop: !0,
            breakpoints: {520: {slidesPerView: 3}, 400: {slidesPerView: 2}}
        }));
        var g = document.querySelector(".modal"), b = document.querySelector(".header__link-sp");
        if (g && b) {
            var S = function () {
                return g.classList.remove("zIndex")
            };
            b.addEventListener("click", (function (e) {
                e.preventDefault(), g.removeEventListener("transitionend", S), g.classList.add("active", "zIndex"), document.body.style.overflow = "hidden"
            })), g.addEventListener("click", (function () {
                this.classList.remove("active"), document.body.style.overflow = "", g.addEventListener("transitionend", S)
            })), g.querySelector(".modal__content").addEventListener("click", (function (e) {
                e.stopPropagation()
            }))
        }

        function L(e, t) {
            (null == t || t > e.length) && (t = e.length);
            for (var r = 0, n = new Array(t); r < t; r++) n[r] = e[r];
            return n
        }

        function E(e) {
            return function (e) {
                if (Array.isArray(e)) return L(e)
            }(e) || function (e) {
                if ("undefined" != typeof Symbol && null != e[Symbol.iterator] || null != e["@@iterator"]) return Array.from(e)
            }(e) || function (e, t) {
                if (e) {
                    if ("string" == typeof e) return L(e, t);
                    var r = Object.prototype.toString.call(e).slice(8, -1);
                    return "Object" === r && e.constructor && (r = e.constructor.name), "Map" === r || "Set" === r ? Array.from(e) : "Arguments" === r || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r) ? L(e, t) : void 0
                }
            }(e) || function () {
                throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
            }()
        }

        if (b && g) {
            var q = E(g.querySelectorAll(".modal__tabs-link")), w = E(g.querySelectorAll(".modal__items-elem"));
            q.forEach((function (e, t) {
                e.addEventListener("click", (function (e) {
                    e.preventDefault(), q.forEach((function (e, t) {
                        e.classList.remove("active"), w[t].classList.remove("active")
                    })), this.classList.add("active"), w[t].classList.add("active")
                }))
            }))
        }
        if (g && b) {
            var A = g.querySelector(".modal__form-signin"), k = g.querySelector(".modal__form-register"),
                x = E(A.querySelectorAll(".modal__form-input")), C = E(k.querySelectorAll(".modal__form-input")),
                I = A.querySelector(".modal__form-btn"), T = k.querySelector(".modal__form-btn"),
                j = k.querySelector(".modal__form-password"), P = k.querySelector(".modal__form-password-rep"),
                O = E(g.querySelectorAll(".modal__form-hide"));
            x.forEach((function (e) {
                e.addEventListener("input", (function () {
                    x.every((function (e) {
                        return "" !== e.value.trim()
                    })) ? I.disabled = !1 : I.disabled = !0
                }))
            })), O.forEach((function (e) {
                e.addEventListener("click", (function (t) {
                    var r = t.target.closest(".modal__form-item"),
                        n = null == r ? void 0 : r.querySelector(".modal__form-input");
                    n && (e.classList.toggle("active"), n.type = e.classList.contains("active") ? "text" : "password")
                }))
            })), C.forEach((function (e) {
                e.addEventListener("input", (function () {
                    C.every((function (e) {
                        return "" !== e.value.trim()
                    })) && j.value === P.value ? T.disabled = !1 : T.disabled = !0
                }))
            }))
        }
        var M = E(document.querySelectorAll(".goods-filters__accordion-name"));
        if (M) {
            var N = M.filter((function (e) {
                var t = e.closest(".goods-filters__accordion-item");
                if (t && t.classList.contains("open")) return e
            })), D = function (e) {
                var t = !(arguments.length > 1 && void 0 !== arguments[1]) || arguments[1], r = e.nextElementSibling,
                    n = e.closest(".goods-filters__accordion-item"), o = r.scrollHeight;
                r && n && !n.classList.contains("open") || !t ? (n.classList.add("open"), r.style.height = "".concat(o, "px")) : r && n && n.classList.contains("open") && (n.classList.remove("open"), r.style.height = "")
            };
            N.forEach((function (e) {
                D(e, !1)
            })), M.forEach((function (e) {
                e.addEventListener("click", (function (t) {
                    t.preventDefault(), D(e)
                }))
            }))
        }
        var V = E(document.querySelectorAll(".single__left-item")), H = document.querySelector(".single__left-show"),
            z = null == H ? void 0 : H.querySelector(".single__left-zoom"),
            U = null == H ? void 0 : H.querySelector("img"), F = function (e, t) {
                return isNaN(Number(e.getAttribute(t))) ? null : Number(e.getAttribute(t))
            };
        U && V && H && z && (V.forEach((function (e) {
            e.addEventListener("mouseenter", (function () {
                var t = e.querySelector("img");
                U.src = t.src, U.style.backgroundImage = t.src, H.setAttribute("data-img", t.src)
            }))
        })), H.addEventListener("mouseover", (function () {
            var e = this.getAttribute("data-img");
            z.classList.add("show"), z.style.backgroundImage = "url(".concat(e, ")")
        })), H.addEventListener("mousemove", (function (e) {
            !function (e, t) {
                var r = e.offsetX, n = e.offsetY, o = r / t.offsetWidth * 100, i = n / t.offsetHeight * 100;
                z.style.backgroundPosition = "".concat(o, "% ").concat(i, "%")
            }(e, this)
        })), H.addEventListener("mouseout", (function () {
            z.classList.remove("show")
        })));
        var R, Y = document.querySelector(".single"),
            B = null == Y ? void 0 : Y.querySelectorAll(".single__right-select");
        B && B.forEach((function (e) {
            e.addEventListener("change", (function (e) {
                var t = e.target.closest(".single__right-chose"),
                    r = null == t ? void 0 : t.querySelector(".single__right-hint-abs");
                r && (r.classList.add("show"), clearTimeout(R), R = setTimeout((function () {
                    R = void 0, r.classList.remove("show")
                }), 2e3))
            }))
        }));
        var J = E(document.querySelectorAll(".self-page__control")),
            W = document.querySelector(".single__content-price span");
        if (J && W) {
            var X = F(W, "data-start-price") || 0, $ = F(W, "data-start-price") || 0;
            J.forEach((function (e) {
                e.addEventListener("change", (function (e) {
                    var t = 0;
                    J.forEach((function (e) {
                        if (e.selectedOptions) {
                            var r = e.selectedOptions[0];
                            if (r) {
                                var n = F(r, "data-price");
                                n && (t += n)
                            }
                        } else if (e.checked) {
                            var o = F(e, "data-price");
                            o && (t += o)
                        }
                    })), W.textContent = (X + t).toLocaleString(), J.forEach((function (e) {
                        if (e.selectedOptions) {
                            var r = e.selectedOptions[0];
                            if (r) {
                                var n = F(r, "data-count");
                                n && ($ = (X + t) * n, W.textContent = $.toLocaleString())
                            }
                        }
                    }))
                }))
            }))
        }
        r(56);
        var G = document.querySelector(".busket-bottom__btn"), K = document.querySelector(".busket-modal"),
            Q = null == K ? void 0 : K.querySelector(".busket-modal__close"), Z = document.querySelector(".busket");
        G && K && Z && (Z.addEventListener("submit", (function (e) {
            e.preventDefault(), K.classList.add("show"), setTimeout((function () {
                K.classList.remove("show")
            }), 3e3)
        })), null == Q || Q.addEventListener("click", (function (e) {
            e.preventDefault(), K.classList.remove("show")
        })));
        var ee = E(document.querySelectorAll(".busket-bottom__label input[type=radio]")),
            te = document.querySelector(".busket-middle__total output");
        if (ee && te) {
            var re = F(te, "data-total");
            ee.forEach((function (e) {
                e.addEventListener("change", (function (e) {
                    var t = F(e.target, "data-percent");
                    if (t && re) {
                        var r = re / 100 * t;
                        te.textContent = (re - r).toLocaleString()
                    } else te.textContent = re.toLocaleString()
                }))
            }))
        }
    }()
}();



