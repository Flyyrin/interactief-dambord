function timeSince(date) {
    var seconds = Math.floor((new Date() - date) / 1000);
    var interval = seconds / 31536000;
    if (interval > 1) {
      return Math.floor(interval) + " jaar";
    }
    interval = seconds / 2592000;
    if (interval > 1) {
      return Math.floor(interval) + " maanden";
    }
    interval = seconds / 86400;
    if (interval > 1) {
      return Math.floor(interval) + " dagen";
    }
    interval = seconds / 3600;
    if (interval > 1) {
      return Math.floor(interval) + " uur";
    }
    interval = seconds / 60;
    if (interval > 1) {
      return Math.floor(interval) + " minuten";
    }
    return Math.floor(seconds) + " seconden";
}