import React from 'react';

// Importance levels match the colour coding in the section study PDFs.
export const IMPORTANCE = {
  HIGH: { label: 'MUST KNOW', className: 'imp-high' },
  MEDIUM: { label: 'IMPORTANT', className: 'imp-medium' },
  LOW: { label: 'BACKGROUND', className: 'imp-low' },
};

export function ImportanceTag({ level }) {
  const meta = IMPORTANCE[level];
  if (!meta) return null;
  return <span className={`imp-tag ${meta.className}`}>{meta.label}</span>;
}
