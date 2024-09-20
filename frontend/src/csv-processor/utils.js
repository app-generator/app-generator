export const getLocalStorageItem = (key, defaultValue) => {
  const savedItem = localStorage.getItem(key);
  return savedItem ? JSON.parse(savedItem) : defaultValue;
};
