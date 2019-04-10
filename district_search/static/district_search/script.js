$(function() {
  $("#drugs").autocomplete({
    source: "/api/get_districts/",
    minLength: 2,
  });
});
