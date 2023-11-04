export const gridProperties = {
  p: 3,
  xs: 12,
  sm: 10,
  md: 8,
  sx: { flexFlow: 'column nowrap', alignItems: 'center', margin: '0 auto', textAlign: 'center' },
};

export function pluralRus(count: number, ...variants: [string, string, string]): string {
  if (count % 10 === 1 && count % 100 !== 11) {
    return `${count} ${variants[0]}`;
  } else if (count % 10 > 1 && count % 10 < 5 && (count % 100 < 10 || count % 100 > 19)) {
    return `${count} ${variants[1]}`;
  } else {
    return `${count} ${variants[2]}`;
  }
}
