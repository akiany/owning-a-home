var supportsAccessors = (function supportsAccessors() {
  var obj = {};
  if ( !Object.defineProperty ) {
    return false;
  }
  try {
    // IE8 incorrectly let's you define properties only on DOM objects.
    Object.defineProperty( obj, 'foo', {} );
    return 'foo' in obj;
  } catch ( e ) {}
})();

// Force it to boolean, we don't want no `undefined` tomfoolery.
module.exports = supportsAccessors ? true : false;
