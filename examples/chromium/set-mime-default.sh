#!/bin/bash
xdg-mime default cnest-chromium.desktop \
  x-scheme-handler/https \
  x-scheme-handler/http

echo To unset, edit ~/.config/mimeapps.list
