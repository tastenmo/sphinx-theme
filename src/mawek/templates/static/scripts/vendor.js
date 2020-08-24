/*! gumshoejs v5.1.2 (patched by @pradyunsg) | (c) 2019 Chris Ferdinandi | MIT License | http://github.com/cferdinandi/gumshoe */
!(function(e,t){"function"==typeof define&&define.amd?define([],(function(){return t(e)})):"object"==typeof exports?module.exports=t(e):e.Gumshoe=t(e)})("undefined"!=typeof global?global:"undefined"!=typeof window?window:this,(function(e){"use strict";var t={navClass:"active",contentClass:"active",nested:!1,nestedClass:"active",offset:0,reflow:!1,events:!0},n=function(e,t,n){if(n.settings.events){var o=new CustomEvent(e,{bubbles:!0,cancelable:!0,detail:n});t.dispatchEvent(o)}},o=function(e){var t=0;if(e.offsetParent)for(;e;)t+=e.offsetTop,e=e.offsetParent;return t>=0?t:0},s=function(e){e&&e.sort((function(e,t){return o(e.content)<o(t.content)?-1:1}))},c=function(t,n,o){var s=t.getBoundingClientRect(),c=(function(e){return"function"==typeof e.offset?parseFloat(e.offset()):parseFloat(e.offset)})(n);return o?parseInt(s.bottom,10)<(e.innerHeight||document.documentElement.clientHeight):parseInt(s.top,10)<=c},i=function(){return Math.ceil(e.innerHeight+e.pageYOffset)>=Math.max(document.body.scrollHeight,document.documentElement.scrollHeight,document.body.offsetHeight,document.documentElement.offsetHeight,document.body.clientHeight,document.documentElement.clientHeight)},r=function(e,t){var n=e[e.length-1];if(function(e,t){return!(!i()||!c(e.content,t,!0))}(n,t))return n;for(var o=e.length-1;o>=0;o--)if(c(e[o].content,t))return e[o]},a=function(e,t){if(t.nested&&e.parentNode){var n=e.parentNode.closest("li");n&&(n.classList.remove(t.nestedClass),a(n,t))}},l=function(e,t){if(e){var o=e.nav.closest("li");o&&(o.classList.remove(t.navClass),e.content.classList.remove(t.contentClass),a(o,t),n("gumshoeDeactivate",o,{link:e.nav,content:e.content,settings:t}))}},u=function(e,t){if(t.nested){var n=e.parentNode.closest("li");n&&(n.classList.add(t.nestedClass),u(n,t))}};return function(o,c){var i,a,f,d,v,m={};m.setup=function(){i=document.querySelectorAll(o),a=[],Array.prototype.forEach.call(i,(function(e){var t=document.getElementById(decodeURIComponent(e.hash.substr(1)));t&&a.push({nav:e,content:t})})),s(a)},m.detect=function(){var e=r(a,v);e?f&&e.content===f.content||(l(f,v),(function(e,t){if(e){var o=e.nav.closest("li");o&&(o.classList.add(t.navClass),e.content.classList.add(t.contentClass),u(o,t),n("gumshoeActivate",o,{link:e.nav,content:e.content,settings:t}))}})(e,v),f=e):f&&(l(f,v),f=null)};var p=function(t){d&&e.cancelAnimationFrame(d),d=e.requestAnimationFrame(m.detect)},h=function(t){d&&e.cancelAnimationFrame(d),d=e.requestAnimationFrame((function(){s(a),m.detect()}))};m.destroy=function(){f&&l(f,v),e.removeEventListener("scroll",p,!1),v.reflow&&e.removeEventListener("resize",h,!1),a=null,i=null,f=null,d=null,v=null};return v=(function(){var e={};return Array.prototype.forEach.call(arguments,(function(t){for(var n in t){if(!t.hasOwnProperty(n))return;e[n]=t[n]}})),e})(t,c||{}),m.setup(),m.detect(),e.addEventListener("scroll",p,!1),v.reflow&&e.addEventListener("resize",h,!1),m}}));